# 1,  查看配置
	CONFIG GET *

# 2, Redis 服务统计信息
	INFO

# 3，安装路径
	CONFIG GET DIR

# 4，查看日志 monitor
	monitor 是redis的监控模式，可以看到redis处理每一个redis请求的，调试模式将影响redis服务性能，所以不建议在线上使用。
	redis-cli monitor | grep '11.10'
# 5, shell operate
	add "XADD" "log:bean:141" "*" "club_id"
		response:'158555-1'
	query XRANGE log:bean:141 - +

	delete XDEL log:bean:141 '158555-1'

# 6， redis缓存数据库
	分类
	确定性缓存 --- 记忆化  --- functools.lru_cache(maxsize, typed) 装饰器 Least recently used， maxsizd 

		设置高速缓存的空间上限，None表示没有限制， typed 定义不同类型的值是否应该被缓存为相同结果。
			给定完全相同输入，确定性函数总是返回相同的值。可以无期限存储他们的结果。 在进程内存中缓存，检索时最快的。
			优化递归函数，针对多次相同的输入进行计算。
		举例：
		查看 fibonacci 数列 第35个fibonacci数列值的计算，不使用缓存对比使用缓存 时间成本是6倍
									使用缓存				不使用缓存
		计算第10个fibonacci数        0.05				0.05
		计算第35个fibonacci数		0.05				6.9
		计算第40个Fibonacci数        0.05				超时....

	非确定性缓存  --- 当不确定他们表示状态是否与其他系统组件（后台服务）状态一致时，一种权衡
		当高速缓存 时间小于 函数时间，那么缓存就是有效的
		适用
		关系型数据库以及常用任何类型的结构化数据存储引擎。
		Web Api 访问的第三方服务
		文件系统，非常频繁访问的文件
		向多个用户提供 数据或服务

	Redis/Memcached
		进程共享相同缓存结果，既减少宝贵的计算资源占用，又解决由多个独立并且不一致的缓存引起的问题。

	总结：以下场景适用
		查询数据库的可调用项的结果
		渲染为静态值的可调用项结果，例如文件内容，Web请求或PDF渲染
		执行复杂计算的确定性可调用对象结果
		全局映射，用于跟踪到期时间的值，如Web会话对象
		需要经常和快速访问的结果

		保存通过Web服务获得的第三代Api结果。 减少延迟





