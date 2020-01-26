import logging
import logging.handlers
import random
import multiprocessing
import time


def listener_configurer():
    """
    定义记录器和日志格式
    :return:
    """
    root = logging.getLogger()
    h = logging.handlers.RotatingFileHandler('mult_test.log', 'a', 300, 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)


def listener_process(queue, configurer):
    configurer()
    while 1:
        try:
            record = queue.get()
            if record is None:  # 哨兵程序，record为None，通知监听器退出
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)  # 没有级别和过滤器设置，
        except Exception as ex:
            import sys, traceback
            print(f"whoops, problem {ex}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)


LEVELS = [logging.DEBUG, logging.INFO, logging.WARNING,
          logging.ERROR, logging.CRITICAL]

LOGGERS = ['a.b.c', 'd.e.f']
MESSAGES = [
    'Random message #1',
    'Random message #2',
    'Random message #3',
]


def worker_process(queue, configurer):
    configurer(queue)
    name = multiprocessing.current_process().name
    print(f'Worker started:%s' % name)
    for i in range(10):
        time.sleep(random.random())
        logger = logging.getLogger(random.choice(LOGGERS))
        level = random.choice(LEVELS)
        message = random.choice(MESSAGES)
        logger.log(level, message)
    print(f'Workder finished:%s' % name)


def worker_configurer(queue):
    h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
    root = logging.getLogger()
    root.addHandler(h)
    # send all messages, for demo; no other level or filter logic applied.
    root.setLevel(logging.DEBUG)


def main():
    queue = multiprocessing.Queue(-1)
    listener = multiprocessing.Process(target=listener_process,
                                       args=(queue, listener_configurer))
    listener.start()
    workers = []
    for i in range(10):
        worker = multiprocessing.Process(target=worker_process,
                                         args=(queue, worker_configurer))
        workers.append(worker)
        worker.start()
    for w in workers:
        w.join()
    queue.put_nowait(None)
    listener.join()


if __name__ == '__main__':
    main()
