# 08-11-back-end 技能
## 原则
   如果在后端程序中有什么不是很需要的立即仍了它。  toss it immediately if sth without a reason.
   或者询问，为何存在于此。    or try to ask why does it exist.
   确保所有东西都有充足的理由存在。 通常背后都有很好的原因。
        keep/make sure everything there is reason. behind it usually it a good reason.
   
   Make cool experiment    做最酷的实验。
   Make strong own opinion  保持强烈信念
   try everything what are you fell intereing  尝试各种有趣的事。
   Dive deep in it     深入你感兴趣的领域。

## 协议  protocal ws， critical as we speal （至关重要）
	传输层，UDP，TCP，web端的大多数协议都是基于这两个传输层协议的上层应用层协议。
	应用层 WebSockets，HTTPS...

		  WebSockets 支持 分别以HTTP的方式访问(ws), HTTPS访问该服务(wss)
		  优点 Prons:
		     全双工，业务包括 多人游戏，多人聊天，文件上传进度，live channal 直播业务等等都可很好的支持
             HTTP compatible， 兼容HTTP(对应ws) 和 HTTPS(对应wss) 访问
             FireWalls firends, standard 防火墙友好，不会启用危险端口
          弱点 Cons:
             1, Proxying is tricky
                 代理支持麻烦，服务器必须响应，代理服务需要支持新的websockets，如nginx
                 当是 L7 /B 第七层应用代理时，nginx必须打破 TLS，终止TLS以检查data，发现协议为http，必须立即创建自己的与服务器的TCP连接，同时需要考虑如何handle
                 同时也需要创建代理与客户端的交互连接。
                 所以成本非常高昂，代理只推荐做负载均衡。 
             2， L7/B challenging timeout应用层代理的超时问题处理。
                 OOP套接字 不应该超时，应该需要保留很长时间的ws连接，这样即使不用也不应为我中断。以保证下一秒用户总是可用的。 即全双工属性。
             3，stateful difficult to horizontally scale  状态机水平扩展能力弱。
                 一旦建立连接，状态就固定无法扩展。
                 如果服务器死机，可以从数据库中读取所有连接并恢复执行。
           使用websocket的场景
           1， 需要全双工通信。 full-duplex
           2，需要长轮询，long polling，用户需要长时间保持在线。
           3，事件驱动。 Event Source
        
 ## 代理 proxy
       反向代理 reverse proxy
       缓存层  caching layers   messaging sys 消息系统的基本原理
          RobitMQ，  
          kafka，    acts like a cue   像一种提示
          ZeroMQ，   消息队列的处理

       固有缓存   inherently caching
       TLS termination  TLS 终止
       atomicity consistoncy  原子性与一致性
       isolation durability   隔离性与耐久性
       Reinforces the ability  增强能力
       
    
## 架构/框架 framwork
    RESTFUL Api
    	an architecture   是一种架构
    	kinds of falls within the framework.  属于框架之内的事。
    	concept    概念
    	web framework very close to a web server   web框架非常接近web服务，
    	more dynamic allows than web server 更具动态灵活性
    	unlock  many potential use   (使用web框架)可以解锁潜在用途。

## 消息协议 message protocal
    essentially send fever bytes as much as possible    尽可能少的在网络中传输信息。
    a human readable of people designed it    人们设计消息协议以方便人类阅读。
    XML   可读性最差
    json   可读性好，更灵活，但是宽带占用较高。 high broadband
    protobuf    宽带使用量合适。 灵活性较高，可读性尚可。  优点: tweak 可调整的。

## 安全性 Security 
    deep into security and proxies       在安全和代理中深入。
    kind of govern most of the stuff     一种统治大多数事物的东西。
    especially encryption in general TLS transport.   特别是通用TLS传输层的加密。
    between Messaging and networking  is security  在信息和网络中是安全的。
    what types of denial attacks:
        stop man-in-middle attacks     阻止中间人攻击
        stop Denial of service attacks   阻止拒绝服务攻击
        sever name indication security   服务器名称是否有安全问题
        database credential not leaked   数据库凭证不可太弱。 

   English Special Term 专用术语/条款
   		Certificate Details    证书细节
   			Certificate Type 证书类别  Domain Validated 域验证（DV）
   			Valid from 有效期始 2020年7月22日05:59:02 GMT Valid to 有效至 2020年10月20日05:59:02 GMT
   			Serial Number 序列号 4f0c1d6922e23843e8290046c7c50bcb11a  0a0141420000015385736a0b85eca708  44afb080d6a327ba893039862ef8406b
   			Algorithm Type 算法类型 SHA256withRSA Key Size 密钥大小 4096
   			Revocation check method 吊销检查方法   OCSP
   			Certificate Transparency logging 证书透明度日志记录  嵌入证书

   		Vulnerabilities    漏洞
   			Vulnerabilities checked    漏洞检查
				Heartbleed, Poodle (TLS), Poodle (SSLv3), FREAK, BEAST, CRIME, DROWN
			Non-critical issues found	非关键问题
				BEAST

				Not mitigated server-side BEAST.  无法缓解服务器BEAST。

   		Certificate  Chain  证书链    
   			login.jjzzapi.com-->Let's Encrypt Authority X3 -> DST ROOT CA x3
   		Server Configuration 服务器配置
   			启用的协议	Protocols enabled
			TLS1.2,TLS1.1,TLS1.0

			协议未启用	Protocols not enabled
			SSLv3,SSLv2

			启用密码套件	Cipher suites enabled
			TLS_RSA_WITH_AES_128_CBC_SHA (0x002F)
			TLS_RSA_WITH_AES_256_CBC_SHA (0x0035)
			TLS_RSA_WITH_AES_128_CBC_SHA256 (0x003C)
			TLS_RSA_WITH_AES_256_CBC_SHA256 (0x003D)
			TLS_RSA_WITH_AES_128_GCM_SHA256 (0x009C)
			TLS_RSA_WITH_AES_256_GCM_SHA384 (0x009D)
			TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (0xC013)
			TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (0xC014)
			TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (0xC027)
			TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (0xC028)
			TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xC02F)
			TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xC030)

			主机名	Host name
			103.147.172.26

			服务器类型	Server Type
			Not available

			IP address
			103.147.172.26

			Port number
			443
		Advanced server Configuration  高级服务配置
			SSL/TLS压缩		SSL/TLS compression   			Not Enabled
			安全重新协商		Secure renegotiation  			Enabled
			会话恢复(缓存)		Session resumption(caching) 	Enabled
			心跳				Heartbeat(extension)			Not Enabled
			降级攻击预防		Downgrade attack prevention    Enabled
			会话恢复(门票) 	Session resumption(tickets)     Enabled
			RC4                             Noe Enabled
			下一级协商	    Next protocol negotiation       Enabled
			严格运输安全		Strict Transport Security(HSTS) UNKNOWN
			OCSP装订			OCSP stapling 					Enabled

## 禁忌
   循环内容过多过大    doing a huge loop
   不要评论别人代码

## 其他，
    算法
    人工智能

    信任链算法。

## 任务task
    二象限                        |       一象限
    算法,区块链                   |  异步协同/并发，os.fork()，asyncio.wait/wait_for/gather     
    AI 应用                       |  同步协同/concurrent.futures(Executor, Future)，异步转同步
    统计学框架                    |  范式,AWS lambda,依赖注入,yml熟练。py自动部署工具fabric     完成
------------------------------------------------------------------------------------
     3象限                      |           4象限
    nginx 代理配置 L4转发，L7转发 |   service local     # 本地服务       
    gitlab/CD                   |    OpenBSD LVS的 L4转发 （软路由）




