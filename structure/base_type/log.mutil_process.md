# 多进程安全日志，进程间RLOC
    logging.FileHandler

# 进程间递归锁

# 多进程安全，多线程安全， 过程安全
    线程安全
    过程安全

# 仅基于公共接口 FileHandler._open()

# 完整的RLock实例接口
    关于threading.RLock 所述(以前没有非阻塞和上下文管理器)
    
    基于Unix/Linux的示例实现，具有基于flock的锁定
        FLockRlock 和 FLockFIleHandler类
    通用抽象类-在开发非Unix平台的实现时可能有用
        MultiprocessRLock, 
        MultiprocessFileHandler
        LockedFileHandler
    MultiprocessRLock.acquire()中非阻塞模式错误
    
# 层次分明的日志实例
    logging.getLogger(__name__)针对包中的每个模块建立的。其他一切都是Handler实例。
    这种设计背后的想法是，它被整齐地划分了。
    您可以方便地查看来自单个记录器的消息，或者查看来自任何记录器或模块的特定级别或更高级别的消息。 
    记录器实例包含每个默认日志级别的输入方法：
    logger.debug()
    logger.info()
    logger.warning()
    logger.error()
    logger.critical()
    还有其他两个日志记录调用：
    logger.log（）：手动发出具有特定日志级别的日志消息。
    logger.exception（）：创建包裹当前异常堆栈帧的ERROR级别的日志消息。
    
    最终记录器，如果一个日志没有被你设置到日志记录器捕获。这些日志会被logging默认到last_record记录
        在定义logger以上内容时，您没有向其添加任何处理程序。那么，为什么要写入控制台呢？
        原因是logging 偷偷使用了一个名为的处理程序lastResort，sys.stderr如果找不到其他处理程序，该处理程序将写入：
     class Logger(Filterer):
    # ...
    def callHandlers(self, record):
        c = self
        found = 0
        while c:
            for hdlr in c.handlers:
                found = found + 1
                if record.levelno >= hdlr.level:
                    hdlr.handle(record)
            if not c.propagate:
                c = None
            else:
                c = c.parent
        if (found == 0):
            if lastResort:
                if record.levelno >= lastResort.level:   # 此处设置记录器级别
                     lastResort.handle(record)   
    如果记录器放弃了对处理程序的搜索（包括它自己的直接处理程序和父记录器的属性），那么它将选择lastResort处理程序并使用该处理程序。    

## 惰性格式 
    重复的日志调用可能会稍微降低运行时性能，但是该logging软件包会尽最大努力来控制它并保持检查状态。通过不立即将格式字符串与其参数合并，
    logging可以延迟字符串格式设置，直到由LogRecord要求Handler。
    LogRecord.getMessage()
    这发生在LogRecord.getMessage()，所以只有后logging认为，该LogRecord实际上将被传递到处理程序，它才会成为其完全合并的自我。

    这就是说，该logging软件包在正确的位置进行了一些非常微调的性能优化。
    这看起来像是细节，但是如果您logging.debug()在一个循环内进行相同的调用一百万次，并且args调用了are函数，则logging字符串格式化的惰性特性可能会有所作为。

    在与msg和进行任何合并之前args，Logger实例将检查其实例.isEnabledFor()，看看是否应该首先进行合并
    
    惰性格式示例
    >>> # Better: formatting doesn't occur until it really needs to.
    >>> logging.warning("To iterate is %s, to recurse %s", "human", "divine")
    WARNING:root:To iterate is human, to recurse divine   
        