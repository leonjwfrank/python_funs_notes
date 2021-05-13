# clould  docker

# 3, docker 方式
          安装docker
                
                3.1, sudo yum install -y yum-utils \
                          device-mapper-persistent-data \
                          lvm2
                3.2, sudo yum-config-manager \
                                --add-repo \
                            https://download.docker.com/linux/centos/docker-ce.repo

                              > repo saved to /etc/yum.repos.d/docker-ce.repo
                $ sudo yum-config-manager --enable docker-ce-test

         3.3,   sudo yum install docker-ce docker-ce-cli containerd.io
                # 查看安装列表
                yum list docker-ce --showduplicates | sort -r

                docker-ce.x86_64  3:18.09.1-3.el7                     docker-ce-stable
                docker-ce.x86_64  3:18.09.0-3.el7                     docker-ce-stable
                docker-ce.x86_64  18.06.1.ce-3.el7                    docker-ce-stable
                docker-ce.x86_64  18.06.0.ce-3.el7                    docker-ce-stable

        3.4,  systemctl start docker
       3.5,   docker run hello-world
                Hello from Docker!
                This message shows that your installation appears to be working correctly.
        参考 https://docs.docker.com/install/linux/docker-ce/centos/

# 4,  构建配置
        4.1 安装docker,win 和mac下载一键安装程序，linux发行版也有响应的安装说明。
                docker version
       4.2  编辑容器配置：
        # docker build -f /path/to/a/Dockerfile .
        Dockerfile
                FROM python:3.6-alpine

                ENV FLASK_APP InnsOwl.py
                ENV FLASK_CONFIG production

                RUN adduser -D  InnsOwl
                USER InnsOwl

                WORKDIR /home/InnsOwl

                COPY requirements requirements
                RUN python3 -m venv venv
                RUN venv/bin/pip install -r requirements/docker.txt

                COPY app app
                COPY migrations migrations
                COPY InnsOwl.py config.py boot.sh ./

                # run-time configuration
                EXPOSE 5000
                ENTRYPOINT ["./boot.sh"]
       4.3  构建容器映像
        docker build -t innsowl:latest .
        
        查看image：docker image
        4.4  运行容器  name 和构建的名称需要一致
                docker run --name innsowl -d -p 8089:8089 -e SECRET_KEY=88f6585a8ea1f705bfe4aae3eb45f6dc2 innsowl:latest
        4.5 确认运行
                docker  ps
        4.6  停止和删除
                docker  stop [name]
                docker  rm   [name]
                docker rm -f [name]   #停止并删除
        4.7 审查运行中的容器
                docker exec -it  [name] sh
        4.8  Docker 引擎日志
                系统        日志位置
                Ubuntu(14.04)        /var/log/upstart/docker.log
                Ubuntu(16.04)        journalctl -u docker.service
                CentOS 7/RHEL 7/Fedora        journalctl -u docker.service
                CoreOS        journalctl -u docker.service
                OpenSuSE        journalctl -u docker.service
                OSX        ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/log/d​ocker.log
                Debian GNU/Linux 7        /var/log/daemon.log
                Debian GNU/Linux 8        journalctl -u docker.service
                Boot2Docker        /var/log/docker.log

        4.9  容器日志
                docker logs 
                容器的日志 则可以通过 docker logs 命令来访问，而且可以像 tail -f 一样，使用 docker logs -f 来实时查看。如果使用 Docker Compose，则可以通过 docker-compose logs <服务名> 来查看。
                docker logs [容器实例ID，CONTAINER ID]

                $ docker run -d –log-driver=fluentd –log-opt fluentd-address=10.2.3.4:24224 –log-opt tag=”docker.{{.Name}}” 
                 配置：
                       docker 日志配置 -D， 默认为；/var/log/messages
                 重定向： dockerd -D >> log_file 2>&1  
                        vim    /etc/docker/daemon.json
                  重启docker  daemon
                        systemctl    docker    stop
                        systemctl    daemon-reload
                        systemctl    start     docker   
                dockerd --log-level debug 
                dockerd -l debug
              查看日志：
                        watch -d -n 1 cat /var/log/messages
            4.10  排查错误
                        启动几秒后自动停止，检查配置文件端口和目录是否正确

# 参考
        https://docs.docker.com/engine/reference/builder/

# 5, 使用外部数据库