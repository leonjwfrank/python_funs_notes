# zmq
	
# 性能对比
	从ORM加载数据并渲染模板返回
	json化一个字段为Json形式，并返回meta为application/json格式

	性能工具
	apache   ab   test
	go-preference-testing
	locustio
	redis 自带工具

1， 从ORM加载数据并json化返回application/json
	web功能计算一个数的阶乘
	与get和post方式请求都只对一个dict字典做json处理并返回application./json

2，logging线程安全
	1，RotatingFileHandler 轮换日志
		限定每个日志文件大小
		限定一定数量的日志文件，不断创建日志文件到该数量时，覆盖掉最开始文件形成循环
	2，多个线程日志记录到单个文件
		logging默认支持
	3，多个进程日志记录到单个文件
		zmq
	4，logger中传递上下文消息
		4.1 传入一个实现了 __getitem__和__iter__的类实例,这样就像一个字典，但是有__iter__方法的实例可以动态生成值，而dict值是固定的
		4.2 filter传递上下文消息
			from random import choise
			class ContextFilter(logging.Filter)
				USERS = ['jims', 'fired', 'shield']
				IPS = ['192.168.0.1', '125.22.112.32', '10.221.21.1']
				def filter(self, record):
					record.ip = choice(ContextFilter.IPS)
					record.user = choice(ContextFilter.USERS)


3, 

