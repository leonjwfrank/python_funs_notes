
# 1.1。基本事件循环
	1.1.1。运行事件循环
		loops = asyncio.get_event_loop()
		loops.run_forever()  # >py3.5
			运行到stop()被调用。 如果stop()在调用前run_forever()被调用，则以零超时对I/O选择器进行一次轮询
			如果stop()在run_forever() 运行时调用，将运行当前一批回调，然后退出。
		loop.run_until_complete()
			运行直到Future完成，如果参数是协程对象。则将其包装未 ensure_future().返回Future结果，或引发异常。
		is_running()   # 事件运行状态。
		stop()        #停止运行事件。   # >py3.5
			调用此函数将导致run_forever()在下一个合适机会退出。
		is_closed()    # 返回True事件循环是否关闭  # >py3.4
		close()      # 关闭事件循环，循环不能正在运行。待处理的回调将丢失。这将清除队列并关闭执行程序，但不等待执行程序完成。
			不可逆。在此之后，不应再调用其他任何方法。
		shutdown_asyncgens()  # >=py3.6
			事件循环将在每次迭代新的异步生成器时发出警告。应该用来可靠完成所有调用的异步生成器。
			try:
				loop.run_forever()
			finally:
			    loop.run_until_complete(loop.shutdown_asyncgens())
			    loop.close()

	1.1.2。调用
		传回关键字
		functools.partial()
		   loop.call_soon(functools.partial(print, 'Hello', flush=True))
		   print("Hello", flush=Trues)
		   # asyncio可检查functools.partial()对象以在调式模式显式参数

		loop.call_soon(callback, *args)
			安排尽快调用回调。 call_soon()当控制权返回事件循环时，在返回之后调用回调，它用作FIFO队列，按注册顺序调用回调。每个回调仅被调用一次
			回调之后的任何位置参数将在调用时传递回调。asyncio.Handle 返回的实例可用于取消回调。
		loop.call_soon_threadsafe(callback, *args)
			类似call_soon()但是线程安全
	1.1.3。延迟调用
		事件循环有自己的内部时钟，用于计算超时。使用哪个时钟取决于事件循环的实现。 理想情况是单调时钟。与time.time()不同
		超时不能超过一天。

		call_later(delay, callback, *args)
		asyncio.Handle 返回的实例可用于取消回调，回调将被完全调用一次call_later()
		可选位置 *args将在调用时传递给回调。 如果需要使用某些命名参数来调用回调请使用闭包或functools.partial()

		call_at(when, callback, *args)
			在给定绝对时间戳(一个整数或浮点数)，使用相同时间基准 loop.time()
			此方法的行为和call_later()相同
			asyncio.Handle返回的实例可用于取消回调。
		loop.time()
			根据事件循环的内部时钟返回当前时间作为值。	参考异步时间模块 asynci.sleep()

	1.1.4。待返
		loop.creaet_future()  # >py3.5
			创建一个asyncio.Future附加到循环的对象。这是在asyncio中创建待返对象的一种首选方法。因为事件循环实现可提供Future类的替代实现。
	1.1.5。任务
		loop.creaet_task()  # 协程对象，>py3.4
			使用协程对象的执行， 将来包装 返回 Task对象
			第三方事件循环可用使用他们自己的Task子类满足互操作性。 返回 一个Task子类
		loop.set_task_factory  # >py3.4
			设置一个供使用的任务工厂 loop.create_task()
			如果工厂是None默认任务，则将设置工厂
			如果factory是可调用的，则应具有签名match 其中loop将是对获得事件循环的引用 coro是协程对象。可调用对象必循返回兼容对象。
			(loop, coro)asyncio.Future
		loop.get_task_factory  # >py3.4
			返回任务工厂，或者None使用默认任务
	1.1.6。建立连接
		loop.create_connection(protocol_factory，host = None，port = None，*，ssl = None，family = 0，proto = 0，flags = 0，sock = None，local_addr = None，server_hostname = None)   # >py3.5
			创建一个流式传输连接到一个给定主机和端口  AF_INET或AF_INET6取决于主机ip版本
			SOCK_STREAM  protocol_factory必须是可调用的可返回协议实例
			协程，将尝试在后台建立连接，成功时，协程返回一对 transport, protocol
			顺序如下：
				1,建立连接，创建一个传输来表示它
				2，调用protocal_factory时不带参数，并且必须返回协议实例
				3，协议实例域传输相关，其connection_made()方法调用
				4，协程与该对象成功返回  transport,protocol
			被创建的传输对象时一个实现相关的双向流。 protocol_factory可用时任何可调用类型 lambda:myprotocol

		loop.create_datagram_endpoint(protocol_factory)  # 协程
			创建一个数据报连接
			创建数据报连接：套接字系列AF_INET或 AF_INET6取决于主机（或系列（如果指定）），套接字类型SOCK_DGRAM。protocol_factory必须是可调用的，可返回协议实例。
			此方法是协程，它将尝试在后台建立连接。成功时，协程返回一对。(transport, protocol)
		loop.create_unix_connection(protocol_factory, path)
			创建UNIX连接，套接字系列 AF_UNIX, 套接字类型SOCK_STREAM所述AD_UNIX使用有效的进程之间进行通信。
			协程，将尝试在后台建立连接，成功时协程返回一对(transport, protocol)
			path是UNIX域套接字的名称，除非 指定了sock参数，否则路径是必需的。支持抽象UNIX套接字，str和 bytes路径。

	1.1.7。建立监听连接
		loop.create_server（protocol_factory，host = None，port = None...)  # >py3.5
		协程，将创建一个SOCK_STREAM绑定到host，port的TCP服务器(套接字类型)
		返回一个Server对象，其sockets属性包含创建的套接字，该Server.close()方法停止服务器。。关闭监听套接字。
		loop.create_unix_server(...)
			协程：类似于creaet_server() 套接字，但特定于 AF_UNIX
		loop.connect_accepted_socket（protocol_factory，sock，*，ssl = None # 》py3.5 ）
			协程：处理可接受的连接。sock 时从accept调用返回的预先存在的套接字对象
			ssl可被设置未一个SSLContext以接受的连接是启用
			返回一对(transport, protocol)
	1.1.8。查看文件描述符
		loop.add_reader（fd，callback，* args ）
			观察文件描述符的读取可用性，然后使用指定的参数调用 回调。
			使用functools.partial将关键字传递给回调
		loop.remove_reader（fd ）

		loop.add_writer（fd，callback，* args ）
			观察文件描述符的写可用性，然后使用指定的参数调用 回调。
			使用functools.partial将关键字传递给回调
		loop.remove_writer(fd)
			停止监视文件描述符的写可用性。

	1.1.9。低级套接字操作
		sock_recv(sock, nbytes)
			协程 从套接字接收数据，在阻塞socket.socket.recv()方法后建模。
			返回值是一个字节对象，代表接收到的数据，一次要接收的最大数据流由bbytes指定
			SelectorEventLoop事件循环，插座必须是非阻塞的。
		sock_sendall(sock, data)
			协程 将数据发送到套接字。 在阻塞socket.socket.sendall()方法后建模
			套接字必须连接到远程套接字，该刚发继续从 data 发送数据，直到所有数据都已发送或发送错误为止。None成功返回
			如果出错，则抛出异常，并且无法确定连接的接收端已成功处理多少数据。
			SelecetorEventLoop事件循环，sock必须是非阻塞的
		sock_connect(sock, address)
			协程 连接到地址为远程套接字，在阻塞socket.socket.connect()方法后创建。
			随着SelectorEventLoop事件循环，sock必须是非阻塞的
			sock_connect 尝试通过调用来检查address是否以及解析socket.inet_pton() 
			如果不是，那么 loop.getaddrinfo()将用于解析地址
		sock_accept(sock)
			协程，接收连接，阻塞后建模 socket.socket.accept()
			此socket必须绑定到一个地址上并且监控连接。返回值是一个元组 （conn, address,其中conn是一个新的套接字对象用于在此连接上收发数据。 *address是连接的另一端的套接字所绑定的地址
			sock对象必须是无阻塞的

	1.1.10。解析主机名
		getaddrinfo(host, port, *, family=0, type=0, proto=0, flags=0)
			协程， 类似 socket.getaddrinfo() 功能但无阻塞
		getnameinfo(sockaddr, flags=0)
			协程，类似 socket.getnameinfo() 功能但无阻塞

	1.1.11。连接管道
		Windows 管道 ProactorEventLoop
		协程   
		connect_read_pipe(protocol_factory, pipe)
			Protocol接口实例化对象，pipe是一个类似文件的对象
			(transport, protocol)ReadTransport
			SelectorEventLoop事件循环，pipe被设置为非阻塞模式
		connect_write_pipe(protocol_factory, pipe)
			在事件循环中注册‘写’管道

	1.1.12。UNIX信号
		add_signal_handler(signum, callback, *args)
			添加信号处理程序
			如果信号数字非法或不可捕获，旧抛出一个ValueError
			使用functools.partial将关键字传递给回调
		remove_signal_handler(sig)
			删除信号处理程序
			如果没有True删除信号处理程序，False则返回

	1.1.13。执行者 Executor
		在Exector（线程池或进程池）中调用函数。默认情况夏事件循环使用线程池执行程序ThreadPoolExecutor
		loop.run_in_executor(executor, func, *args)
			 协程，安排在指定执行程序中调用func
			 在下hi参数应该是一个Executor实例。如果executor则使用默认executor 为None
			 使用functools.partial将关键字传递给func
		loop.set_default_executor(executor)
			设置所使用的默认执行程序 run_in_executor()
	1.1.14. 错误处理API
		允许自定义事件循环中如何取处理异常
		loop.set_exceotion_handler(executor)
			把handler设置为新的实践循环异常处理器
			如果handler为None，则将设置默认的异常处理程序
			如果处理程序是可调用对象，则它应具有匹配的签名，其中将是对获得事件循环的引用，将是一个对象（有关上下文的详情）
			(loop, context) loop contextdict call_exception_handler()

		loop.get_exception_handler()  # >py3.5
			返回异常处理程序，或者None使用默认处理程序
		loop.default_exception_handler()  # 默认的异常处理器
			默认的异常处理器
			发送异常且未设置任何异常处理程序时，将调用此方法。并且可用由想要遵从的默认行为自定义异常处理程序进行调用
			context参数和call_exception_handler() 中的同名参数完全相同
		loop.call_exception_handler(context)
			调用当前事件循环的异常处理器
			context是一个dict包含以下键的对象
			message: 错误消息
			exception 可选：异常对象
			future 可选：asyncio.Future 实例
			handler 可选: asyncio.Handler 实例
			protocol 可选：Protocol实例
			transport 可选：Transport实例
			socket可选：socket.socket实例

			此方法不应在子类事件循环中重载，对应任何自定义异常处理请使用set_exception_handler() 方法

	1.1.15。调试模式
		loop.get_debug()   # >py3.4
		获取事件循环调式模式设置(bool)
		如果环境变量PYTHONASYNCIODEBUG 是一个非空字符串，返回True，否则返回False
		loop.set_debug()   # >py3.4

	1.1.16。服务器 Server
		不要直接实例化Server类，loop.Server()  # 错误
		AbstractEventLoop.create_server()
			close()
				停止服务：关闭监听的套接字并设置sockets为None
				用于表示以及连接的客户端，连接将保持打开的状态。
				服务器时被异步关闭的，使用wait_closed()协程等待服务器关闭
			wait_closed()
				等待closed()方法执行完成，协程
			sockets
				socket.socket 服务器正则侦听对象列表，或者None服务器已关闭
		AbstractEventLoop.start_server()

	1.1.17。处理 Handle
		asyncio.Handle
			通过返回回调包装对象 AAbstractEventLoop.call_soon(), AbstractEventLoop.call_soon_threadsafe(),
			AbstractEventLoop.call_later(), AbstractEventLoop.call_at()
		cancle()
			取消调用，如果回调已被取消或执行，此方法无效。
	1.1.18。事件循环示例
		AbstractEventLoop.call_soon()方法安排示例
		import asyncio
		def hell_world():
			print(f"Hi, World")
			loop.stop()
		loop = asyncio.get_event_loop()
		# Schedule a call to hello_world()
		loop.call_soon(hell_world, loop)
		loop.run_forever()
		loop.close()

	1.1.18.1. call_soon() 的 Hello World 示例。
	1.1.18.2. 使用 call_later() 来展示当前的日期
		def display_data(end_time, loop)
			# 1:delay time, display_data:self-call, end_time: *args 
			loop.call_later(1, display_data, end_time, loop)
		loop.call_soon(display_data, end_time, loop)  # 回调

	1.1.18.3. 监控一个文件描述符的读事件
		使用socket程序简单示例 from socket import socketpair, 该scoketpair方法将返回(接收端，发送端)元组
		rsock, wsock = socketpair()

		事件主循环添加数据读取者
		def reader():...   # socket接收处理函数
		    data = rsocks.recv(100)
		    print(f"data:{data.decode()}")
		    loop.remove_reader(rsocks)
		loop.add_reader(rsock, reader)   #添加读取者

		loop.call_soon_threadsafe(wsock.send, 'abc'.encode())  #socket 数据发送者
		# 关闭对象
		rsock.close()
		wsock.close()
		loop.close()

	1.1.18.4. 为SIGINT和SIGTERM设置信号处理器
		仅适用类UNIX系统
# 1.2. 事件循环
	1.2.1. 事件循环函数
		全局策略方法访问的便利快捷方式，默认方法
		asyncio.get_event_loop()
			等价于调用get_event_loop_policy().get_event_loop()
		asyncio.set_event_loop()
			等价于调用get_event_loop_policy().set_event_loop()
		asyncio.new_event_loop()
			等价于调用get_event_loop_policy().new_event_loop()

	1.2.2. 可用的事件循环
		asyncio 当前提供两种事件循环实现 
		SelectorEventLoop 

		ProactorEventLoop

	1.2.3. 平台支持
		asyncio在不同平台有不同的特点，细微的区别。
	1.2.3.1。视窗
		SelectorEventLoop 

		ProactorEventLoop
	1.2.3.2。Mac OS X
		10.6 以后开始支持
		默认的事件循环是 SelectorEventLoop 

	1.2.4. 事件循环策略和默认策略
		一般不需要自定义的显示处理事件循环策略，默认的全局策略以及够用。
		模块级的get_event_loop 和 set_event_loop 是对应默认策略管理事件循环的遍历访问。

	1.2.5. 事件循环策略接口
		一个事件循环必须实现如下接口
		class asyncio.AbstractEventLoopPolicy: 中的
			def get_event_loop()
				为上下文获取事件循环
			def set_event_loop()
				将当前上下文事件循环设置为loop
			def new_event_loop()
				根据策略规则创建并返回新的事件循环对象
				如果有需要设置这个循环作为当前上下文事件循环，必须显式调用 set_event_loop()

	1.2.6. 访问全局循环策略
		asyncio.get_event_loop_policy()
		获取当前事件循环策略
		asyncio.set_event_loop_policy(policy)
		设置当前事件循环策略，如果policy为None，将恢复使用默认策略

		主事件循环在一次运行只会启动一个实例，类似单例

	1.2.7. 自定义事件循环策略
		实现一个新的事件循环策略，即自定义，需要继承具体的默认事件循环策略DefaultEventLoopPolicy并且改写行为方法
		class MyEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
			def get_event_loop(self):
				"""This may be None or an instance of EventLoop."""
				loop = super().get_event_loop()
				return loop
		asyncio.set_event_loop_policy(MyEventLoopPolicy())

# 1.3。任务和协程
	源码位置
		Lib/asyncio/tasks.py
		Lib/asyncio/coroutines.py

	1.3.1. 协程 asyncio.Future
		此类几乎兼容 concurrent.futures.Future

	1.3.1.1。示例：Hello World协程
	1.3.1.2。示例：协程显示当前日期
	1.3.1.3。示例：链式协程
		协程函数里调用了其他协程
	1.3.2。InvalidStateError
		不允许的操作错误
	1.3.3。TimeoutError
		TimeoutError 这里与py内置的 TimeoutError异常不同
	1.3.4。未来 asyncio.Future

	1.3.4.1。示例：带有run_until_complete（）的Future
		协程函数赋值计算，耗时1s， 并将结果存储到Future。 run_until_complete()方法等待将来完成。
		run_until_complete()方法在内部使用add_done_callback()将来完成时要通知的方法。

	1.3.4.2。示例：带有run_forever（）的Future
		与run_until_complete(future) 类似，都使用ensure_future(func(future))（包装协程或 待返的未来对象）
		不同的是，run_forever 需要手工调用future.add_done_callback 添加一个获取结果的回调函数。
		而 run_until_complete() 调用后直接获取结果 future.result()

		run_forever() 需要先添加回调，然后调用run_forever(), 才能使用future.result()来获取 待返对象的结果。  如果没有添加回调，不会有结果/ 如果在执行run_forever()前 获取future结果，返回错误 InvalidStateError:Result is not set.

	1.3.5。任务 
		asyncio.Task(coro, *, loop=None)
	        安排协程任务
	        all_tasks(loop=None)   # classmethod 返回事件循环中所有任务集合，默认为当前事件循环
	        current_task(loop=None)  # classmethod 在事件循环中返回当前正在运行的任务
	        cancel()       # 请求此任务自行取消安排 CanceledError通过事件循环在下一个周期将a放入包装好的协程。
	            #调用此方法后，cancelled()将不会立即返回True 除非任务取消，当包装的协程CancelledError异常终止，即使cancel()未调用，任务将被标记已取消
	        # 
	        get_stack(*, limit=None)  # 返回此任务协程的堆栈帧列表，如果协程未完成，将其挂起的堆栈返回。 如果协程已成功完成或被取消，则返回一个空列表。如果协程被终止返回回溯帧列表。
	        print_stack()   # 打印此任务的协程的堆栈或回溯，对于get_stack()检索到的帧，将产生与回溯模块相似的输出，limit参数传递给get_stack() 
	            file参数是将输出写入其中的I/O流，默认将写入sys.stderr
	            
			 asyncio.as_completed(fs, *, loop=None, timeout=None)  # 返回一个迭代器，等待时值未Fture实例
	        如果Future对象完成前发生超时将引发 asyncio.TimeoutError
	        for f in as_completed(fs):
	            result = yield from f  # The 'yield from ' may raise

	1.3.5.1。示例：并行执行任务
		asyncio.gater   # 收集任务传播给主事件循环，收集结果，返回给Future
	1.3.6。任务功能
		Task功能：
		asyncio.ensure_future(coro_or_future，*，loop = None)
			安排协程对象的执行：将来包装它。返回一个Task对象。

			如果参数为Future，则直接返回。
	   asyncio.as_completed(fs, *, loop=None, timeout=None)  # 返回一个迭代器，等待时值未Fture实例
        如果Future对象完成前发生超时将引发 asyncio.TimeoutError
        for f in as_completed(fs):
            result = yield from f  # The 'yield from ' may raise
    
       asyncio.gater(*coros_or_futures, loop=None, return_exceptions=False)  # >py3.6.6
        # 从给定的协程对象或 待返对象(future)汇总结果
        # 所有期货碧玺共享相同事件循环，如果所有任务都成功完成，则返回future结果就是结果列表（按原始序列的顺序，不一定时结果到达顺序）
        # 如果外部任务Future被取消，所有子任务也将取消。
        # 如果任何子任务被取消，该子任务被视为CancelledError这种情况，外部Future不会取消

       asyncio.iscoroutine()
       	 如果obj 时协程对象，返回True，
       asyncio.iscoroutinefunction(func)
       	  如果func被确定为协程函数，返回True。 协程函数可用时修饰的生成器函数/
       asyncio.run_coroutine_threadsafe(coro, loop)   #>py3.5
       	  把协程对象提交到给定的事件循环。 返回一个concurrent.futures.Future以访问结果
       	  该函数应该从与事件循环不同的线程中使用
       	  coro = asyncio.sleep(1, result=3)   # 创建协程
       	  fut = asyncio.run_coroutine_threadsafe(coro, loop)  # 提交协程到事件循环
       	  assert fut.result(timeout) == 3      # 断言等待
       asyncio.sleep(delay, result=None, *, loop=None)

       asyncio.shield(arg, *, loop=None)  # 等待待返结果，免受取消
       	result = yield from shield(sth())
       	完成等同于 result = yield from sth()
       	# 如果sth() 通过其他方式取消，将取消 shield()
       	# 如果包含shield的协程被取消，其中运行的任务sth()不会取消
       	# 完成忽略取消
       	try:
       		res = yield from shield(sth())
       	except CancelledError:
       		res = None

       	asyncio.wait(futures, *, loop=None,...)   # 等待序列中的协程对象完成，协程将包装在任务中返回两套Future
       	# 等待序列不能为空。

       	asyncio.wait_for(fut, timeout, *, loop=None)
       	# 等待单个Future 或协程对象完成超时，如果timeout为None，则阻塞直到 待返（future） 完成
       	协程被包裹在 Task里
       	返回Future或协程的结果，发生超时，将取消任务

# 1.4。传输和协议（基于回调的API）
	1.4.1. 传输
		# asyncio 传输和协议 基于回调的API控制
		# 源代码 Lib/asyncio/transports.py
		# 协议源代码 Lib/asyncio/protocols.py
		# 一旦建立传输通道，传输总是与协议实例配对。然后协议可用出于各种目的调用传输器方法。
		支持协议包括 TCP，UDP，SSL，子进程管道传输。

	1.4.1.1。基础传输
		asyncio.BaseTransport
			close(), is_closing(), get_extra_info(name, default=None)... 
			set_protocol(protocol), get_protocol

	1.4.1.2。传输的读操作
			asyncio.ReadTransport

	1.4.1.3。写操作
			asyncio.WriteTransport
	1.4.1.4。数据报传输
				DatagramTransport
			DatagramTransport.sendto(data, addr=None)
			DatagramTransport.abort()

	1.4.1.5。BaseSubprocessTransport
				asyncio.BaseSubprocessTransport
			get_pid()
			get_pipe_trandport(fd)
	1.4.2. 协议
	1.4.2.1。协议类别
	1.4.2.2。连接回调
	1.4.2.3。流协议
		在Protocol实例上调用以下回调：

		Protocol.data_received(data)
		收到一些数据时调用。 data是包含输入数据的非空字节对象
	1.4.2.4。数据报协议
	1.4.2.5。流控制回调
	1.4.2.6。协程和协议
	1.4.3。协议实例
	1.4.3.1。TCP回显客户端协议
	1.4.3.2。TCP回显服务器协议
		coro = loop.create_server(EchoServerProtocol, '127.0.0.1', 888)
		server = loop.run_until_complete(coro)
		loop.run_forever()
	1.4.3.3。UDP回显客户端协议
		connect = loop.create_datagram_endpoint(lambda:EchoClientProtocolUDP(msg,loop), remote_addr=('127.0.0.1', 9999))
		loop.run_until_complete(connect)
	1.4.3.4。UDP回显服务器协议
		listen = loop.create_datagram_endpoint(EchoServerProtocolUDP, local_addr=('127.0.0.1', 9999))
		loop.run_until_complete(listen)
	1.4.3.5。注册一个开放的套接字以使用协议等待数据, 基于事件主循环的回调
		from socket import socketpair
		class Myprotocol(asyncio.Protocol):
			rsock, wsock = socketpair()
			conn_coro = loop.create_connection(Myprotocol, sock=self.rscok)
 			trans, proto = loop.run_until_complete(conn_coro)
 			loop.call_soon_threadsafe()
 			loop.run_forever()

# 1.5。流（基于协程的API）
	1.5.1。流功能
        asyncio.open_connection
		asyncio.start_server
		asyncio.open_unix_connection
		asyncio.start_unix_server
	1.5.2。StreamReader
		asyncio.StreamReader(limit=_DEFAULT_LIMIT, loop=None)
			非线程安全 限制参数的默认值设置为 _DEFAULT_LIMIT=2**16 (64kb)
			exception  # 异常的获取
			feed_eof   # 确认EOF错误，Read beyond end of file. 可能是读取文件或者循环体中读写长度错误
			feed_data(data)   # 在内部缓冲区馈送数据字节，等待数据的所有操作将恢复
			set_exception(exc) #设置例外
			set_transport(transport)  # 设置传输方式

			async read(n=-1)   #读取n个byte如果没有设置n，自动设置为-1，读至 EOF并返回所有读取的byte，如果读取为空，则返回一个空bytes对象

			async readexactly(n)   # 精确读取n个字节， IncompleteReadError如果在可以将读取n之前达到流的末尾，引发IncompleteReadError.partial异常，属性包含部分读取的字节
			async readuntil(eparator=b'\n)  #>py3.5 # 从流中读取数据，直到separator为止,如果发生EOF仍然找不到完整分隔符，引发异常IncompleteReadError,并重置内部缓冲区。
	1.5.3。StreamWriter
		流的异步协程处理,功能
		asyncio.StreamWriter(transport, protocol, reader, loop)      
			# 非线程安全
			transport  #运输
			write()      # 向传输(transport)写入一些数据字节
			writelines()   # 将数据字节列表(或任何可迭代字节)写入传送器
			can_write_eof()  # 如果运输工具支持write_eof()返回True ，否则返回 False
			write_eof()
			get_extra_info()   # 返回可选的运输信息
			close()				# 关闭运输工具 BaseTransport.close()
			
			async drain()   # 返回的可选Future内容。 让基础传输的写缓冲区有机会被刷新

		asyncio.StreamReaderProtocol(stream_reader，client_connected_cb = None，loop = None)
			帮助器类，不是使StreamReader字节成为Protocol子类
			在Protocol和StreamReader之间适应子类Protocol
			stream_reader是一个StreamReader实例
		asyncio.IncompleteReadError
			读取错误不完成，子类的EOFError
			expected   预期字节总数 int
			partial    到达流的结尾 bytes 之前读取字节字符
		asyncio.LimitOverunError
			consumed   要消耗的字节总数
	1.5.4。StreamReader协议
	1.5.5。IncompleteReadError
		asyncio.IncompleteReadError  #读取错误不完整，是EOFError的子类
		expected   预期字节总数 int
		partial    达到流的结尾 bytes
	1.5.6。LimitOverrunError
		寻找分隔符时已达到缓冲区限制
		consumed   # 要消耗的字节总数
	1.5.7。流示例
		asyncio.start_server()    # TCP回显服务器
	1.5.7.1。TCP回显客户端使用流
	1.5.7.2。使用流的TCP回显服务器
	1.5.7.3。获取HTTP头
	1.5.7.4。注册一个打开的套接字以使用流等待数据,基于异步api
		@asyncio.coroutine
		def wait_for_data(loop):
			# Create a pair of connected sockets
    		rsock, wsock = socketpair()
    		# Register the open socket to wait for data
    		reader, writer = yield from asyncio.open_connection(sock=rsock, loop=loop)
    		# Simulate the reception of data from the network
		    loop.call_soon(wsock.send, 'aaa'.encode())

		    # Wait for data
		    data = yield from reader.read(100)

		    # Got data, we are done close the socket
		    print(f"Received:{data.decode()}")
		    writer.close()

		    # Close the second socket
		    wsock.close()

# 1.6。子流程
	1.6.1。Windows事件循环
		windows另一种事件循环
		if sys.platform == 'win32':
			loop = asyncio.ProactorEventLoop()
			asyncio.set_event_loop(loop)
		or
		loop.asyncio.get_event_loop()

	1.6.2。创建一个子流程：使用流程的高级API
		协程 asyncio.create_subprocess_exec(*args, stdin=None, stdout=None, stderr=None, loop=None,limit=None)   # 创建子进程，返回一个Process实例
		
		协程 asyncio.create_subprocess_shell(cmd, stdin=None, stdout=None,stderr=None,loop=None,limit=None,**kwds)   #运行shell的 指令

	1.6.3。创建一个子流程：使用subprocess.Popen的低级API
		使用subprocess模块异步运行子流程
		协程 AbstractEventLoop.subprocess_exec(protocol_factory, *args, stdnii=subprocess.PIPE....)
			# 从一个或多个字符串参数创建子进程，其中第一个字符串指定要执行的程序。其他字符串指定程序的参数。
			# protocol_factory必须实例化一个子类 asyncio.SubprocessProtocol
		协程 AbstractEventLoop.subprocess_shell(protocol_factory, cmd, *,....)
			# 使用平台的shell语法从cmd创建一个子进程	
	1.6.4. 常量
		asyncio.subprocess.PIPE
			# 可用使用为特殊值标准输入，标准输出或标准错误create_subprocess_shell()和create_subprocess_exec()和表示的管，以标准的流应该被打开
		asyncio.subprocess.STDOUT
			# 可用作and 的stderr参数的特殊值 指示标准错误与标准输出进入同一句柄create_subprocess_shell()
		asyncio.subprocess.DEVNULL
			# 可用为and的stdin，stdout或stderr参数的特殊值 create_subprocess_shell()

	1.6.5。进程Process	 # 不是线程安全
		class asyncio.subprocess.Process
			# create_shubprocess_exec() 或 create_subprocess_shell()函数创建的子流程
			# Process该类的API被设计为与该类的API接近subprocess.Popen但是存在一些差异
				# 没有明确的poll()方法， communicate()和wait()方法不采取超时参数 始于wwait_for()功能
				# wait()所述方法Process，类是异步wait()方法Popen类作为繁忙循环中实现
		asyncio wait   # 协程
			等待进程终止，设置并返回returncode属性
			# 使用stdout=PIPE，或 stderr=PIPE导致死锁，并且子进程将向管道生成足够的输出，从而阻塞等待OS管道缓冲区接受更多数据的等待。
		asyncio communicate(input=None)
			# 与进程交互，将数据发送到stdin
			# 从stdout，stderr读取数据，直到达到文件末尾。等待进程终止。
		send_signal(signal)
			# 将信号发送到子进程
		terminate()
			# 阻止子进程Posix OS上该方法发送signal.SIGTERM给子进程，在windows将调用Win32 API函数 TerminteProcess()来停止子级
		kill()
			# 杀死子进程，该功能将发送SIGKILL给子级。
		stdin/stdout/stderr  #标准输入流，标准输出流，标准错误流
		pid  #进程标识符
		returncode   # 退出时返回进程代码
	1.6.6。子进程和线程
		asyncio支持从不同线程运行子进程，但有些限制
			# 事件循环必须在主线程运行
			# 从其他线程执行子进程之前，必须在主线程中实例化子监视程序
			# get_child_watcher()在主线程中调用该函数以实例化子进程观测者。
			asyncio.subprocess.Process类不是线程安全的
	1.6.7。子流程示例
	1.6.7.1。使用传输和协议的子流程
		继承自asyncio.SubprocessProtocol
		class DateProtocol(asyncio.SubprocessPtotocol)
		覆写 pipe_data_received， process_exited
		# 调用
		@asyncio.coroutine
		def get_date(loop):
			...
			create = loop.subprocess_exec(lambda: DateProtocol(exit_future),
                                  sys.executable, '-c', code,
                                  stdin=None, stderr=None)
    		transport, protocol = yield from create
    		...

	1.6.7.2。使用流的子流程
	@asyncio.coroutine
	def get_dates():
		...
		create = asyncio.create_subprocess_exec(sys.executable, '-c', code, stdout=asyncio.subprocess.PIPE)
	    proc = yield from create
	    # Read one line of output
	    date = yield from proc.stdout.readline()
	    line = date.decode('ascii').rstrip()
	    # Wait for the subprocess exit
	    yield from proc.wait()
	    ...

# 1.7。同步原语 Synchronization primitives
	锁：
		Lock
		Event
		Condition
	信号量：
		Semaphore
		BoundedSemaphore
		ASYNCIO锁API被设计成接近的类threading 模块（Lock，Event， Condition，Semaphore， BoundedSemaphore），但它没有超时参数。该 asyncio.wait_for()功能可用于在超时后取消任务。
	1.7.1。锁具
	1.7.1.1。锁 Lock
		class asyncio.Lock(*, loop=None)   # 非线程安全
			# 原始锁对象，基元锁是一种同步基元。
			# 原始锁只处于锁定 解锁两种状态 
			  # 协程 已获得 acquire(),  与yield from 一起使用
			  # release()
			yield from lock  # 锁支持上下文管理协议。应该用作上下文管理表达式

		# 获得锁
		lock = Lock()
		...
		yield from lock
		try:
			...
		finally:
		# 释放锁
		    lock.release()

		# 上下文管理器
		lock = Lock()
		....
		with (yield from lock):
		   ...

		# 测试锁定对象的锁定状态
		if not lock.locked():
		    yield from lock
		else:
		   # lock is acquired

		功能
		是否获得锁 locked()   # 如果获得了锁，返回True
		协程 获取锁 acquire()
		释放锁 release()
        
	1.7.1.2。事件 Event
		class asyncio.Event(*, loop=None)   # 非线程安全
			# Event 实现，异步等效于 threading.Event,实现事件对象的类。事件管理一个标志(默认为false)，该标志可用通过方法设置为true，并通过set()设置为false 
		    clear()   # 内部标志位重置false，协程调用wait()将阻塞到set()被调用以再次将内部标志设置位true
		    is_set() #True当且仅当北部标志为true才返回
		    set()  # 将内部标志设置为true
		    wait()   # 协程

	1.7.1.3。 触发条件 Condition
		class asyncio.Condition(lock=None, *, loop=None)  # 非线程安全
			# 条件实现，异步等效于threading.Condition
			此类实现条件变量对象，条件变量运行一个或多个协程等待，直达他们被另一个协程通知
			如果没有给出lock参数为None，则必须是一个Lock对象，并且用作基础锁，否则将Lock创建一个新对象并将其用作基础锁
		    
		    协程 acquire()    # 获取基础锁，此方法将阻塞到解锁，然后再将其设置为lock并返回True

		    notify(n=1)   #默认情况夏，唤醒一个协程等待这个情况(如果有)如果在调用此方法时调用协程尚未获取锁定 引发错误 RuntimeError

		    locked()   # 如获得了基础锁，则返回

		    notify_all()   # 唤醒等待这种情况的所有协程。此方法类似 notify() 但此方法是唤醒所有等待的协程，如果调用此方法时被调用协程尚未获取锁定，则触发 RuntimeError

		    release()   # 无返回，释放基础锁，将其重置为解锁状态然后返回。未锁定的锁被调用时，引发RuntimeError
		    asyncio wait()   # 等到收到通知，如果调用此方法时协程尚未获取锁定，RuntimeError将触发
		    	# 此方法释放基础锁，然后进行阻塞 直到被notify()等类似方法唤醒为止。唤醒后，它将重新获取锁并返回True
		    asyncio wait_for(func)  # 等到func变为真，func应为可调用的，结果解释为布尔值

	1.7.2。信号量 Semaphores

	1.7.2.1。信号
			class asyncio.Semaphore(value=1, *, loop=None)   # 非线程安全
			# 信号量实现。 此类管理一个内部计数器，计数器由每个acquire()调用递减，并由每个release()调用递增。计数器永远不能低于0，当acquire()发现它为0时，将阻塞，直到其他协程调用release() 为止。
			asyncio acquire()    #获取一个信号量，如果内部计数器在输入时大于零，将其递减一，并返回True。如果进入时为0，阻塞；等待其他协程调用release() 使其大于0，然后返回True

			locked()   # 如果无法立即获取信号量返回 True

			release()   # 释放信号量，使内部计数器加1，进入时为0，并且另一个协程正则等待再次变为0，唤醒该协程
	1.7.2.2。有界信号量
			class asyncio.BoundedSemaphore(value=1, *, loop=None)
				# 有界信号量实现，继承自Semaphore。 在release() 它是否将增加超过ValueError初始值的值
# 1.8. 队列集
	源代码： Lib / asyncio / queues.py
		Queue
		PriorityQueue
		LifeQueue
		ASYNCIO队列API被设计为接近的queue模块的类 asyncio.wait_for() 功能可用于在超时 后取消任务
	1.8.1. 队列
		class asyncio.Queue(Maxsize=0, *, loop=None)   # >py3.44
			# 队列用于协程生产者和消费者协程，如果maxsize小于或等于零，队列大小无限。 如果maxsize大于0，当队列达到maxsize时将阻塞，直到被删除 yield from 
			put(), get()
			与标准库不同queue，可用可靠的知晓Queue的大小qsize()，因为单线程asyncio应用程序不会在 调用qsize()和在Queue上执行操作时被中断。
			empty()  # 如果队列为空返回True，否则返回False
			full()   # 如果有maxsize个条目在队列，则返回True。 如果Queue使用参数maxsize=0， 则full()用于不会为True
			协程 get()  #从队列删除并返回一个元素。如果队列为空，则等待，直到队列有元素
			 get_nowait()  #从队列中删除并返回一个项目，立即返回一个队列中的元素，如果队列有值，引发异常QueueEmpty
			协程 join()   # 阻塞直到队列所有项目都已获得并处理，每当将项目添加到队列时，未完成任务数量将增加。
				# 当未完成任务数降至0，join() 取消阻止
			协程 put()  #  项目放入队列。如果队列已满，请等待空闲插槽可用再添加到项目
			put_nowait()  # 不阻塞的放一个元素入队列。如果没有空闲槽位，引发QueueFull异常
			qsize()   # 队列中的项目数
			task_done() # >py3.4.4  
				# 表面前面排队的任务已经完成，即get出来的元素相关操作已经完成。
 			maxsize  # 队列中可存放的元素数量

	1.8.2。PriorityQueue
		class asyncio.PriorityQueue
			子类Queue，以优先级顺序检索条目 从低到低，条目通常是以元组形式 （优先级，数据）
	1.8.3。LifoQueue
		class asyncio.LifoQueue
			# 子类Queue首先检索最近添加的条目
	1.8.3.1. 异常
		asyncio.QueueEmpty
			get_nowait() 时，Queue为空对象时引发
		asyncio.QueueFull
			put_nowait() 在Queue已满的对象上调用该方法时引发异常
# 1.9。用asyncio开发
	1.9.1。异步调试模式
	1.9.2。消除
	1.9.3。并发和多线程
	1.9.4。正确处理阻止功能
	1.9.5. 日志记录
	1.9.6。检测从未调度的协程对象
	1.9.7。检测从未消耗的异常
	1.9.8。正确协程
	1.9.9。待处理任务已销毁
	1.9.10。关闭传输和事件循环

# 2.0. asyncore -异步socket处理器
	2.1  asyncore Example basic HTTP client
	2.2  asyncore Example basic echo server

# 3.0. asynchat -异步socket指令/响应 处理器
	3.1 asynchat Example
# 4.0. signal  -设置异步事件处理程序
    4.1 一般规则
    	4.1.1 执行Python信号处理程序
    	4.1.2 信号与线程
    4.2 模块内容
    4.3 示例
# 5.0. mmap    -内存映射文件支持
    

# 6 练习
	asyncio 异步聊天室

