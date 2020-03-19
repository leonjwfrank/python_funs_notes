# 1，虚拟机 virtual  machine带环境安装的一种解决方案
        缺点：资源占有多
                    虚拟机独占一部分内存和硬盘空间，运行时其他程序就不能使用这些资源，哪怕虚拟机应用程序只使用内存1m，整个虚拟机也要几百MB才能运行。        
                   冗余步骤多
                   虚拟机是完整的操作系统，一些系统级别的操作步骤如登陆不能跳过
                   启动慢
                    操作系统启动需要几分钟
# 2，linux容器（linux containers，LXC）
                不是模拟一个完整的操作系统，而是对进程进行隔离，正常进程外面套来一个保护套，对容器内的进程来说，它接触到的资源都是虚拟的，从而实现与底层系统的隔离，进程级别相对虚拟机有很多优点：1，启动快，2，资源占用少，3，体积小

# 3， docker 是linux容器的一种封装，提供简单易用的容器使用接口，目前最流行的linux容器解决方案。
        docker 将应用程序与该程序依赖打包在一个文件里（image），运行这个文件就会生成一个虚拟容器，程序在这个虚拟容器运行，就好像是在真是物理机运行。
        接口简单，Docker的接口简单，方便创建和使用容器，把自己的应用放入容器。容器还可以进行版本管理，复制，分享，修改，就像管理普通代码易用。
# 4， Docker用途
        提供一次性环境，本地测试他人软件，持续集成时提供单元测试和构建的环境
        提供弹性云服务，Docker容器可以随开随关，适合动态扩容和缩容
        组建微服务架构，通过多个容器，一台机器可以跑多个服务，本机就可以模拟出微服务架构

# 5，Docker 社区版和企业版
        验证安装 docker version/info
        启动docker服务才能执行docker指令
        # service      sudo service docker start， 
        # systemctl    sudo systemctl start docker
        
        image文件， docker image ls                      #列出所有image
        容器文件，   docker container ls --all        #列出所有包括终止运行的容器
        docker container kill [name] / docker stop  [name]   #终止容器运行
        docerk container rm [name] / docker rm -f   [name]  #停止并删除容器
        
# 6， 制作image的Dockerfile文件
        1，排除路径文件写入文件
                .dockerignore
                        .git
                        node_modules
                        npm-debug.log
        2,    Dockerfile文件内容
                FROM  node:8.4           # 该image文件继承官方node image，冒号表示标签，8.4，即8.4版本node
                COPY .  /home/app        # 将当前目录下所有文件(排除.dockerignore文件中注明的路径)都拷贝进入image文件的/home/app
                WORKDIR  /home/app  #指定路径
                RUN pip3 install --        # 在指定路径下安装依赖，安装后的依赖都将打包进入image文件
               EXPOSE  8089                # 将容器8089端口暴露出路，运行外部连接这个端口
        3， docker image build  -t  name   #创建image
        4，生成容器  docker  container  run  命令会从image文件生成容器
                docker  container run -d -p 8089:5000  -it innsowl:0510img  /bin/bash
                -it 参数：        容器shell映射到当前shell，然后你在本机窗口输入的命令就会传入容器
                /bin/bash            # 容器启动后，内部第一个执行的命令，这里是启动Bash，保证用户可以使用shell
        5， 发布image文件
                容器运行成功后，就确认来image文件的有效性，image分享到网上
                docker login
                docker image tag [imageName] [username]/[repository]:[tag]    #为本地image标注用户名和版本
                #重新构建一下image文件
                docker image build -t [username]/[repository]:[tag]
                #发布
                docker image push [username]/[repository]:[tag]
                #发布成功后，登录 hub.docker.com

# 7,其他指令
        1，docker container start    #启动要重复使用的容器
        2，docker container stop    #停止容器
        3，docker container logs    #查看容器的输出，即容器里面shell的标准输出，如果docker run 命令运行容器的时候没有使用-it参数，就需要使用这个命令查看输出
        4，docker container exec   #命令用于进入一个正在运行的docker容器，一旦进入容器就可以执行shell
                docker exec -it mysql bash
                
        5，docker container cp      # 将Docker容器的文件拷贝到本机
        6，docker pause/unpause   #暂停/恢复容器所有进程
    
        7, 重复使用
            #启动之前创建的容器
                    docker start [Name of container]

    #进入启动的容器
                    docker attach [Name of container]
             pip3  uninstall paddlepaddle


# 8， 微服务创建
        1，软件把任务外包出去，让各种外部服务完成这些任务，软件本身只是底层服务的调度中心组装层。
        2，每一个docker容器安装一个服务，如数据库容器，业务容器，各容器把端口和服务暴露出来，在一台机器上可以实现多个服务。




        