# nginx 在docker中的配置修改
## 安装
 	docker search nginx
	docker pull nginx
	docker run --name nex-nginx -p 801:801 -v /some/content:/usr/share/nginx/html:ro -d nginx    
	#-v 挂载本地目录到容器。 -p 表示内部801端口映射到外部801端口，:ro 表示只读，可用本地磁盘， -d 表示后台运行

	docker ps   # 查看nginx id
	docker exec -it cd6f4a3c4c24 /bin/bash

	# 进入nginx 容器 bash


## 文件移动
	将docker容器对象 文件传输到主机当前目录
		docker cp cd6f4a3c4c24:/etc/nginx/nginx.conf ./
	将主机文件 传输到docker 容器对象
		docker cp  ./game-591.conf cd6f4a3c4c24:/etc/nginx/conf.d/

