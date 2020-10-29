# 多线程
	多线程可以实现任务高并发执行任务，但是也会有死锁，GIL锁限制等问题

# 多进程
## 特点
	高性能
	不受限于GIL 全局解释器锁
	适合多核心处理器的计算机
	进程间不共享内存上下文
	避免死锁
## 创建
	linux 等 POSIX系统中
		os.fork
	windows
		multiprocessing
	内置的Process类可以使用在任何平台
	from multiprocessing import Process
## 进程间同步接口
	multiprocessing 进程间通信模式
	    multiprocessing.Queue , 类似于Treading 线程间通信的queue.Queue近似克隆,有相同的接口
	    multiprocessing.Pipe,   类似于套接字socket的双向通信通道，类似Unix管道
	    multiprocessing.sharedctypes, 在进程间共享专有内存池中创建任意C类型 ---> 从ctypes模块

## 进程间同步原语
	信号量



# 异步/协程
	可以看作时类似线程但不涉及系统调度的技术。 而且上下文在内部，而不是由系统调度程序切换。

	协同多任务和异步I/O   cooperative multitasking 异步编程的核心。
	启动上下文切换（到另一个进程或线程）不是操作系统的责任，二十每个进程在空闲时字典释放控制以允许同时执行多个程序。 所以称为协同
	所有进程需要协同才能处理多任务。

	区别于 python的线程模式，操作系统可以抢占py多线程的时间，但是在异步中任务不会被主事件循环抢占，所以又称为：
	非抢占式多任务 non-preemptive multitasking
	如果系统调度程序抢占了 该异步程序的处理时间，当异步应用程序运行回来时，它将从相同位置继续运行，仍然可以任务时非抢占式。
	例1：
	async def async_hi(n):  # 构建定义一个新的 协程。  协程函数的执行可以在严格定义夏 暂停和恢复， 语法和行为于 yield生成器相似。
		print(f"hi, guys, {n}")
	当执行 async_hi()  他们不执行里面代码，而返回一个协程对象。 需要事件循环调度该任务执行后，协程将执行其内容
		ioloop = asyncio.get_event_loop()
		loop.run_until_complete(async_hi())
		loop.close()
	例1没有并发，真正的并发多任务可以使用loop.create_task()方法
	或者通过使用asyncio.wait()函数提供另一个对象将 来等新任务添加到循环中。
	例2：
	wait 把任务 async_hi() 添加到 事件循环中
		ioloop = asyncio.get_event_loop()
		loop.run_until_complete(asyncio.wait([async_hi(n) for n in range(5)])  # 产生5个任务异步执行
		loop.close()

	# 官方文档 asyncio.task  https://docs.python.org/zh-cn/3/library/asyncio-task.html
	asyncio.gather             # 并发的执行任务
		async def main():
    		# Schedule three calls *concurrently*:
    		await asyncio.gather([])
	asyncio.wait     # 函数接受协程对象列表并立即返回。 结果是参数表示未来结果 futures的对象生成器。 用于等待所有的协程完成，返回一个生成器（兼容）
		并发运行 aws 指定的 可等待对象 并阻塞线程直到满足 return_when 指定的条件。
		返回两个 Task/Future 集合: (done, pending)
	asyncio.wait_for # 超时，可等待对象在指定 timeout 秒数后超时。 
	asyncio.shell    # 保护一个可等待对象防止被 取消。
		不同之处 在于如果包含它的协程被取消，在 something() 中运行的任务不会被取消。从 something() 的角度看来，取消操作并没有发生。然而其调用者已被取消，因此 "await" 表达式仍然会引发 CancelledError。
		如果通过其他方式取消 something() (例如在其内部操作) 则 shield() 也会取消。

		如果希望完全忽略取消操作 (不推荐) 则 shield() 函数需要配合一个 try/except 代码段

	await			# 用于等待协程或未来 future的结果，并释放事件循环的执行控制

## 事件循环的操作
	
	loop.call_soon_threadsafe(callback, *args, context=None)¶
	call_soon() 的线程安全变体。必须被用于安排 来自其他线程 的回调

## futures 将异步代码同步化
	concurrent.futures 
		Executors     #并行处理工作项的资源池 类似于multiprocessing Pool 和 Dummy.Pool 但是有完全不同的接口和语义
			有一个虚基类，不可实例化，两个具体实现
			ThreadPoolExecutor    # 线程池
			ProcessPoolExecutor   # 进程池
			每个池执行者有三个方法
			submit(fn, *args, **kwarg)     # 将资源池上执行调度db函数返回Future对象，该对象表示可调用执行 ，返回 Future对象
				from concurrent.futures import TheadPoolExecutor
				with ThreadPoolExecutor(1) as executro:
				future = executor.submit(loudy_return)
				future.result()    #  立即查看结果
			map(func, *iterables, timeout=None, chunksize=1)    # 在一个迭代器上执行func函数，类似multiprocessing.Pool.map()用法
			shutdown(wait=True)    # 将关闭执行程序并释放所有资源
		futures


# 异步/协同开发


## 常见异步asyncio开发陷阱
	调试模式
	loop1 = asyncio.get_event_loop()
	loop1.set_debug(enabled=True)

    loop1.run_until_complete(await_main())

    调式对象
    	协程已定义，但是从未 产生
    	从错误的线程调用  call_soon() , call_at() 该方法将抛出错误
    	记录选择器的执行时间
    	日志回调需要花费100ms 执行， AbstractEventLoop.slow_callback_duration属性是“慢速”回调的最小持续时间（以秒为单位）
    	ResourceWarning 如果没有明确关闭传输和事件循环，发出警告


### 定义异步任务后，需要取消任务
	同步编程中，取消任何很少见，异步编程中这很常见
	Future.cancel()   # 明确取消
	wait_for()      # 发生超时

	在等待 future时，应该尽量检查是否cancel，例
	@coroutine
	def slow_operation(fut):
		if fut.cancelled():   # 检查是否取消
			return
		# ...slow computation
		yield from fut

	shield()  # 可以忽略取消

## 并发和多线程
	来自其他线程的回调
	loop.call_soon_threadsafe(callback, *args)
	大多异步对象不是线程安全的，如果要取消Future，不要使用 Future.cancel(),而是应该
	loop.call_soon_threadsafe(fut.cancel)		# 为了能正确处理信号与执行子进程，事件循环必须运行在主线程中

	future = asyncio.run_coroutine_threadsafe(coro_func(), loop)   # run_coroutine_threadsafe 返回 concurrent.futures.Future对象
	result = future.result(timeout)  # Wait for the result with a timeout

## 正确关闭锁和日志级别设定
	阻塞函数不应直接调用。例如，如果某个功能阻塞1秒钟，则其他任务将延迟1秒钟
	执行程序可用于在不同线程甚至不同进程中运行任务，而不阻塞事件循环的线程。参见 AbstractEventLoop.run_in_executor()


	那些不希望asyncio日志级别如此详细的人，可以更改。例如，将级别更改为logging.WARNING： logging.getLogger('asyncio').setLevel(logging.WARNING)

## 检测从未调度的协程对象
	调用协程函数并且其结果未传递到方法ensure_future() 或传递给AbstractEnentLoop.create_task()方法时，协程对象永远不会被调度。
	错误示例：
	@asyncio.coroutine
	def test():
		print(f"test")







