# 目录
    小册
    1   开篇：RPC 要解决的核心问题和在企业服务中的地位
    2   基础：深入 RPC 交互流程
    3   协议 1：深入 RPC 消息协议
    4   协议 2：Redis 文本协议结构
    5   协议 3：Protobuf 二进制协议结构
    6   协议 4：Redis 协议的缺陷
    7   客户端：深入 RPC 客户端设计
    8   服务器 1：【单线程同步】模型
    9   服务器 2：【多线程同步】模型
    10  服务器 3：【多进程同步】模型
    11  服务器 4：【PreForking同步】模型
    12  服务器 5：【单进程异步】模型
    13  服务器 6：【PreForking异步】模型
    14  服务器 7：【多进程描述符传递】模型
    15  分布式 1：深入 RPC 分布式原理
    16  分布式 2：分布式 RPC 知识基础
    17  分布式 3：分布式 RPC 实战
    18  拓展 1：gRPC 原理与实践
    19  拓展 2：Thrift 原理与实践
    20  深入理解 RPC : 基于 Python 自建分布式高并发 RPC 服务
    服务器 6：【PreForking异步】模型
    单个进程的 IO 并发能力有限，虽然使用了事件轮询 API 和异步读写功能，但是还是不够应对大型服务的高并发要求。特别是 Python 这种语言因为 GIL 的存在使得单个进程只能榨干一个 CPU 核心。我们需要一种扩展机制可以扩大服务器的整体并发处理能力，好好利用现代处理器的多核优势，这就需要使用多进程。

    将 PreForking 机制和事件轮询异步读写结合起来，就能达成上面扩展的目标。PreForking 出来的每个子进程内部都是一个事件循环，一个进程可以榨干一个 CPU 核心，多个进程就可以榨干多个 CPU 核心。

    ![](E:\work\Node\Days_Node\async_fork.jpg)


    多进程 PreForking 异步模型
    代码实现和前面的单进程异步模型差别不大，就是多了个 prefork 调用。prefork 在服务器套接字启用监听队列之后进行，这样每个子进程都可以使用服务器套接字来获取新连接进行处理。




```python
 ``coding: utf8

import json

import struct

import socket

import asyncore

from cStringIO import StringIO

import os

class RPCHandler(asyncore.dispatcher_with_send):  # 客户套接字处理器必须继承 dispatcher_with_send

	def __init__(self, sock, addr):
    	asyncore.dispatcher_with_send.__init__(self, sock=sock)
    	self.addr = addr
    	self.handlers = {
        "ping": self.ping
    	}
    	self.rbuf = StringIO()  # 读缓冲区由用户代码维护，写缓冲区由 asyncore 内部提供

	def handle_connect(self):  # 新的连接被 accept 后回调方法
    	print self.addr, 'comes'

	def handle_close(self):  # 连接关闭之前回调方法
    	print self.addr, 'bye'
    	self.close()

	def handle_read(self):  # 有读事件到来时回调方法
    	while True:
        	content = self.recv(1024)
        	if content:
            	self.rbuf.write(content)
        	if len(content) < 1024:
            	break
    	self.handle_rpc()

	def handle_rpc(self):  # 将读到的消息解包并处理
    	while True:  # 可能一次性收到了多个请求消息，所以需要循环处理
        	self.rbuf.seek(0)
        	length_prefix= self.rbuf.read(4)
        	if len(length_prefix) < 4:  # 不足一个消息
            	break
        	length, = struct.unpack("I", length_prefix)
        	body = self.rbuf.read(length)
        	if len(body) < length:  # 不足一个消息
            	break
        	request = json.loads(body)
        	in_ = request['in']
        	params = request['params']
        	print os.getpid(), in_, params
        	print in_, params
            handler = self.handlers[in_]
            handler(params)  # 处理消息
            left = self.rbuf.getvalue()[length + 4:]  # 消息处理完了，缓冲区要截断
            self.rbuf = StringIO()
            self.rbuf.write(left)
    	self.rbuf.seek(0, 2)  # 将游标挪到文件结尾，以便后续读到的内容直接追加

    def ping(self, params):
        self.send_result("pong", params)

    def send_result(self, out, result):
        response = {"out": out, "result": result}
        body = json.dumps(response)
        length_prefix = struct.pack("I", len(body))
        self.send(length_prefix)  # 写入缓冲区
        self.send(body) # 写入缓冲区..
   
class RPCServer(asyncore.dispatcher):  # 服务器套接字处理器必须继承 dispatcher
	def __init__(self, host, port):
    	asyncore.dispatcher.__init__(self)
    	self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    	self.set_reuse_addr()
    	self.bind((host, port))
    	self.listen(1)
    	self.prefork(10)  # 开辟 10 个子进程

	def prefork(self, n):
    	for i in range(n):
        	pid = os.fork()
        	if pid < 0:  # fork error
            	return
        	if pid > 0:  # parent process
            	continue
        	if pid == 0:
            	break  # child process...

	def handle_accept(self):
    	pair = self.accept()
    	if pair is not None:
        	sock, addr = pair
        	RPCHandler(sock, addr)
if name == 'main':
	RPCServer("0.0.0.0", 28080)
	asyncore.loop()``

```




开源框架 Tornado 和开源代理服务器 Nginx 正是采用了多进程 PreForking 异步模型达到了业界啧啧称奇的高并发的处理能力。

同步模型 vs 异步模型
同步和异步的差别就好比卡车和摩托车一样，如果遇到了交通堵塞，卡车只能继续等待堵塞缓解才可以继续前进。但是摩托车不一样，它可以切换到其它小路不停地往前开。...

 