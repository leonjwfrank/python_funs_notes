# zeromq依赖库
	zeromq
		消息队列 http://zeromq.org/area:download
		功能 主要用于日志由内存落地到文件的过程
		过程: 生产者进程，游戏服务器进程-->内存-->zeromq-->消费者进程(日志进程)保存
		优点: 生产者避免了文件写I/O开销，提高服务器性能

		python版本
			pip install pyzmq,
			导入  import zmq
			分服务端(接收)和客户端(发送)两个部分


# protobuf
	协议缓存，编写要存储的数据结构的.proto描述。
	protobuf支持以某种格式扩展，以便代码仍可以读取以旧格式编码的数据。

## 下载: https://github.com/protocalbuffers/protobuf/releases
	protobuf-python-3.11.2.zip
	protoc-3.11.2-win64.zip   ===win10 版本

## 安装
	解压到C盘， 
	设置环境变量 使用户在任何地方都可以使用protoc这个指令. 在path添加 c:\Program Files\protoc-3.11.2-win64\bin

## 测试安装
	打开命令操作符 输入 protoc --version, 如果正常将输出版本号

## 读写操作
	在项目路径创建包路径  hello_protobuf/protobuf/
	在pychram创建addressbook.proto
	syntax = "proto3" 
	message Person {
		string name=1;
		int32 id = 2;
		string email = 3;
		enum PhoneType{
		MOBILE = 0;
		HOME = 1;
		WORK = 2;
		}
	message PhoneNumber{
		string number =1;
		PhoneType type =2;
	}
	repeated PhoneNumber phones = 4;
	}
	message AddressBook {
	repeated Person people =1;
	}


3, 编译
	protoc -python_out =./ addressbook.proto
	生产的/protobuf/addressbook_pb2.py就是需要使用的协议文件


4，关键字与修饰词
	除非确定一个字段会被设置，否则使用optional代替required
		required    #该值一定需要设置
		optional	#该字段可以为0或1个值，不超过1
		repeated    #该字段可以重复0~n次

	标量类型  string
	结构化数据
		message是Protobuf的结构化数据，类似 class 可以在其中定义需要处理的数据
		package声明一个包名，防止不同消息类型命名冲突，类似namespace
		syntax = 'proto3' 表示protobuf编译器版本3
		//注释 类型于#

# 业务逻辑，game逻辑，玩家管理 继承自实体类Entity与子类Component
	Blackboard， Match...

# 进程间操作
	进程间通信
		peer-to-peer的程序同时又client process 与 server process
		发送，接收消息通过socket进行
	进程寻址
		进程接收消息标识符，ip地址，主机上的进程端口号，在此基础上的其他路径或资源
	应用层通信协议
		共有协议: RFCs中定义，允许互相操作，http，smtp等
		私有协议 QQ，skype等

		X维护状态协议：1，需要维护过去的状态，2：需要在C/S崩溃后state不一致时仍能恢复
		HTTP
		非持久http，一次tcp连接最多一个对象
		持久http，一次tcp可以发生多个对象，http1.1



# socket
	websocket wss:443, ws:80
	stress_module request.fetch(r,callback=success)-->request.fetch(r)

	redis性能 apache 软件qt
	


