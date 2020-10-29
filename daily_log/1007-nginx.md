# Nginx 

	四大模块
	proxy、
		1）proxy_pass URL;
			Context: location, if in location, limit_except
			 
			注意：proxy_pass后面的路径不带uri时，其会将location的uri传递给后端主机
			server {
			    …
			    server_name HOSTNAME;
			 
			    location /uri/ {
			       proxy http://hos[:port];
			       }
			 
			       …
			       }
			 
			http://HOSTNAME/uri –> http://host/uri

		2) proxy_pass后面的路径是一个uri时，其会将location的uri替换为proxy_pass的uri
 
			server {
			    …
			    server_name HOSTNAME;
			 
			    location /uri/ {
			        proxy http://host/new_uri/;
			        }
			        …
			        }
			 
			http://HOSTNAME/uri/ –> http://host/new_uri/

		3) 如果location定义其uri时使用了正则表达式的模式，则proxy_pass之后必须不能使用uri; 用户请求时传递的uri将直接附加代理到的服务的之后
			server {
			    …
			    server_name HOSTNAME;
			        location ~|~* /uri/ {
			        proxy http://host;
			        }
			        …
			        }
			 
			http://HOSTNAME/uri/ –> http://host/uri/

		2）proxy_set_header field value;
			设定发往后端主机的请求报文的请求首部的值；Context: http, server, location
			 
			proxy_set_header X-Real-IP  $remote_addr;
			$remote_addr：记录的是上一台主机的IP，而上一台主机有可能也是代理服务器
			 
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			    $proxy_add_x_forwarded_for：记录的是源IP地址
			 
			在http客户端还有修改/etc/httpd/conf/httpd.conf文件
			LogFormat "%{X-Real-IP}i %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
			通过上述方法则可以在后端主机上记录真实的httpd资源请求者，而不再是只记录前端代理服务器的IP地址
			 
			 
		3）proxy_cache_path
			定义可用于proxy功能的缓存；Context:    http
			 
			proxy_cache_path path [levels=levels] [use_temp_path=on|off] keys_zone=name:size [inactive=time]
			[max_size=size] [manager_files=number] [manager_sleep=time] [manager_threshold=time] [loader_files=number]
			[loader_sleep=time] [loader_threshold=time] [purger=on|off] [purger_files=number] [purger_sleep=time] [purger_threshold=time];
			 
			proxy_cache_path /var/cache/nginx/proxy_cache levels=1:2:1 keys_zone=gmtest:20M max_size=1G;
			 
		4）proxy_cache zone | off;
			指明要调用的缓存，或关闭缓存机制；Context: http, server, location
			proxy_cache gmtest;
			 
		5）proxy_cache_key string;
			缓存中用于“键”的内容；
			默认值：proxy_cache_key $scheme$proxy_host$request_uri;
			 
			建议定义成方法和url
			 
		6）proxy_cache_valid [code …] time;
			定义对特定响应码的响应内容的缓存时长；
			 
			定义在http{…}中；
			proxy_cache_path /var/cache/nginx/proxy_cache levels=1:1:1 keys_zone=gmtest:20m max_size=1g;
			 
			定义在需要调用缓存功能的配置段，例如server{…}，或者location中；
			proxy_cache gmtest;
			proxy_cache_key $request_uri;
			proxy_cache_valid 200 302 301 1h;
			proxy_cache_valid any 1m;
			 
			 
		7）proxy_cache_use_stale
			proxy_cache_use_stale error | timeout | invalid_header | updating | http_500 | http_502 | http_503 | http_504 | http_403
			| http_404 | off …;
			 
			Determines in which cases a stale cached response can be used when an error occurs during communication with the proxied server.
			 
			后端服务器的故障在那种情况下，就使用缓存的功能对客户的进行返回
			 
			 
		8）proxy_cache_methods GET | HEAD | POST …;
			If the client request method is listed in this directive then the response will be cached. “GET” and “HEAD” methods are always
			added to the list, though it is recommended to specify them explicitly.
			 
			默认方法就是GET HEAD方法
			 
			 
		9）proxy_hide_header field;
			By default, nginx does not pass the header fields “Date”, “Server”, “X-Pad”, and “X-Accel-…” from the response of a proxied server
			to a client. The proxy_hide_header directive sets additional fields that will not be passed.
			 
		10）proxy_connect_timeout time;
			Defines a timeout for establishing a connection with a proxied server. It should be noted that this timeout cannot usually exceed 75
			seconds.
			 
			默认为60s
			 
			 
		11）buffer相关的配置
			a：proxy_buffer_size size;
			Sets the size of the buffer used for reading the first part of the response received from the proxied server. This part usually contains
			a small response header. By default, the buffer size is equal to one memory page.
			 
			默认为4k|8k
			b：proxy_buffering on | off;
			Enables or disables buffering of responses from the proxied server.
			 
			默认为on
			c：proxy_buffers number size;
			Sets the number and size of the buffers used for reading a response from the proxied server, for a single connection. By default, the buffer size is equal to one memory page.
			 
			默认为8 4k|8k
			d：proxy_busy_buffers_size size;
			When buffering of responses from the proxied server is enabled, limits the total size of buffers that can be busy sending a response to the client while the response is not yet fully read.


			 
			默认为8k|16k



	headers、
		The ngx_http_headers_module module allows adding the “Expires” and “Cache-Control” header fields, and arbitrary fields,
to a response header.
		向由代理服务器响应给客户端的响应报文添加自定义首部，或修改指定首部的值；
		1）add_header name value [always];
		添加自定义首部；
		add_header X-Via  $server_addr;
		经由的代理服务器地址
		add_header X-Accel $server_name;
		 
		2）expires [modified] time;
		expires epoch | max | off;
		 
		用于定义Expire或Cache-Control首部的值；
		可以把服务器定义的缓存时长修改了；	


	upstream、
		7层代理
				The ngx_http_upstream_module module is used to define groups of servers that can be referenced by the proxy_pass, fastcgi_pass,
		uwsgi_pass, scgi_pass, and memcached_pass directives.
		 		
			1）upstream name { … }
				定义后端服务器组，将引入一个新的上下文；Context: http
			 
				upstream httpdsrvs {
				            server …
				            server…
				            …
				}
			 
			 
			2）server address [parameters];
				在upstream上下文中server成员，以及相关的参数；Context: upstream
				 
				address的表示格式：
				unix:/PATH/TO/SOME_SOCK_FILE
				IP[:PORT]
				HOSTNAME[:PORT]
				 
				parameters：
				weight=number
				权重，默认为1；默认算法是wrr
				 
				max_fails=number
				失败尝试最大次数；超出此处指定的次数时，server将被标记为不可用
				 
				fail_timeout=time
				设置将服务器标记为不可用状态的超时时长
				 
				max_conns
				当前的服务器的最大并发连接数
				 
				backup
				将服务器标记为“备用”，即所有服务器均不可用时此服务器才启用
				 
				down
				标记为“不可用”
				 
				先在nginx前端配置down，然后在下架后端服务器，上架新的web程序，然后上架，在修改配置文件立马的down
			 
			 
			3）least_conn;
				最少连接调度算法，当server拥有不同的权重时其为wlc
				要在后端服务器是长连接时，效果才好，比如mysql
			 
			 
			4）ip_hash;
				源地址hash调度方法
			 
			 
			5）hash key [consistent];
				基于指定的key的hash表来实现对请求的调度，此处的key可以直接文本、变量或二者的组合
			 
				作用：将请求分类，同一类请求将发往同一个upstream server
			 
				If the consistent parameter is specified the ketama consistent hashing method will be used instead.
				 
				示例：
				hash $request_uri consistent;
				hash $remote_addr;
				hash $cookie_name; 对同一浏览器的请求，发往同一个upstream server
			 
			 
			6）keepalive connections;
				为每个worker进程保留的空闲的长连接数量
				 
				nginx的其它的二次发行版：
				tengine
				OpenResty
			 
			1.9版本之后可以反代tcp／udp的协议，基于stream模块，工作与传输层

	stream模块
		ngx_stream_core_module模块 实现Nginx的TCP负载均衡
		4层代理，TLS，需要Nginx 1.9.0
		upstream为通常所说的 七层负载均衡，工作在第七层应用层。而TCP负载均衡工作在网络层和传输层。例如，LVS(Linux Virtual Server Linux虚拟服务)和FS(一种硬件负载均衡)属于四层负载均衡。
		1) 配置Nginx编译文件参数
		./configure --with-http_stub_status_module --with-stream
		-------------------
		2) 编译，安装 make&& make install
		-------------------
		3) 配置nginx.conf 文件
			stream {
				upstream kevin {
					server 192.168.10.10:8080;   # 这里配置为要访问的地址
					server 192.168.10.30:8081;   # 需要代理的端口，在这里我代理一个kevin模块的接口8081
				}
				server {
					listen 8081;     # 需要监听的端口
					proxy_timeout  20s;
					proxy_pass kevin;
				}
			}
		创建最高级别的stream(与http同一级别)，定义一个upstream组，名称为kevin，由多个服务组成达到负载均衡，定义一个服务用来监听TCP连接端口。
		并把他们代理到一个upstream组的kevin中，配置负载均衡的方法和产生为每个server:连接数，权重等。

		首先创建一个server组，用来作为TCP负载均衡组。定义一个upstream块在stream上下文中，在这个块里添加server命令定义的server主机名(能够被解析成多地址的主机名)
		和端口好。下面的例子是建立一个被称之为kevin组，两个监听1395端口的server一个监听8080端口
		upstream kevin {
			server   192.168.10.10:8080;	#这里配置称要访问的地址
			server   192.168.10.20:8081;
			server   192.168.10.30:8081;    #需要代理的端口，在这里我代理一一个kevin模块的接口8081
		}


# L7 配置举例
	游戏配置 在 nginx默认配置的上一级,如 /usr/local/nginx/conf/game
		center.conf: 
		upstream gate {
			hash sremote_addr consistent; #会话保持
			server    127.0.0.1:8900 weight=5 max_fails=3 fail_timeout=30s;
		}
		server {
			listen   8990 ssl;
			server_name  localhost;  # substitute your machine's IP address or FQDN
			ssl_certificate        /usr/local/nginx/ssl/127.0.0.1:89.crt;
			ssl_certificate_key    /usr/lcaol/nginx/ssl/127.0.0.1:89.key;
			# max upload size
			client_max_body_size 75M;    # adjust to taste

			location / {
						proxy_http_version 1.1;
						proxy_set_header   Upgrade $http_upgrade;
						proxy_set_header   Connection "upgrade";
			proxy_pass    http:/gate;
			}
		}
	游戏配置 game98.conf
		Upstream game_586 {
			hash $remote_addr consistent    # 会话保持
			server    127.0.0.1:8701 weight=5 max_fails=3 fail_timeout=30s;
		}

		Server {
			listen  8771 ssl;
			server_name localhost; # substitute your machine's IP address or FQDN
			charset    utf-8;
			ssl_certificate 	/usr/local/nginx/ssl/127.0.0.1:81.crt;
			ssl_certificate_key /usr/local/nginx/ssl/127.0.0.1:81.key;

			location / {
						proxy_http_version 1.1;
						proxy_set_header   Upgrade $http_upgrade;
						proxy_set_header   Connection "upgrade";
			proxy_pass    http:/game_666;
			}
		}
	添加配置到目录  在 /usr/local/nginx/conf/nginx.conf
	   include game/*.conf


# LVS 4层代理
	实现七层负载均衡的软件有：
		haproxy：天生负载均衡技能，全面支持七层代理，会话保持，标记，路径转移；
		nginx：只在http协议和mail协议上功能比较好，性能与haproxy差不多；
		apache：功能较差
		Mysql proxy：功能尚可。

		总的来说，一般是LVS(Linux Virtual Server)做4层负载；nginx做7层负载(也能做4层负载, 通过stream模块)；haproxy比较灵活，4层和7层负载均衡都能做
			

		不能为每个Server定义协议，stream命令做为建立TCP的整个协议。

		-  七层负载均衡基本都是基于http协议的，适用于web服务器的负载均衡。（nginx）
		-  四层负载均衡主要是基于tcp协议报文，可以做任何基于tcp/ip协议的软件的负载均衡。(haproxy、LVS)


# 
	
	
