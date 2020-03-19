# docker mongo 
# 1， docker search mongo
# 2， 拉取官方镜像
        docker pull mongo  
# 3， 查看本地镜像
        docker  images mongo
# 4，  创建目录mongo 存储数据库等,db目录将映射为mongo容器配置的 /data/db目录，作为mongo数据的存储目录
         mkdir -p  ~/mongo  ~/mongo/db
# 5，   通过Dockerfile创建一个镜像， 查询镜像
         docker build  -t mongo:3.2 .      docker image list
        # 或者不用再创建镜像，直接使用pull获取的
        docker run --name mongodb -v ~/docker/mongo:/data/db -p 27017:27017 -d mongo

# 6,     使用镜像，运行容器
        docker run -it  mongo:3.2 mongo  --host  127.0.0.1:27017
        docker run -p 27017:27017 -v $PWD/db:/data/db  -d  mongo:3.2
        -p   端口映射
        -v    路径映射，$PWD/db:/data/db   将主机当前目录的db挂载到容器/data/db，作为mongo数据存储目录
        
        # 检查端口是否启动成功
                netstat -an | grep 27017
                        tcp6       0      0  ::1.27017              *.*                    LISTEN    
                        tcp4       0      0  *.27017                *.*                    LISTEN7，使用mongo镜像执行mongo命令连接到刚启动的容器，主机为本机
        
        docker exec -it mongodb bash
        # 使用交互形式，在名字为mongodb的容器中实行bash命令

# 8， 开始使用
        docker exec -it mongodb bash    # 进入mongo交互模式
        1，创建用户和数据库
                mongo                        # 进入mongo
                use admin                  # 切换admin数据库
                # 创建管理员用户
                db.createUser({user:"admin",pwd:"123456",
                                        roles:[{role:"userAdminAnyDatabase", db: "admin" }])
                # admin数据库中插入数据，并且查询结果
                 use admin
        switched to db admin
        > db.info.find();
        > db.info.save({name:'Jack',role:'root'})
        WriteResult({ "nInserted" : 1 })
        > db.info.find();
        2019-05-11T03:26:49.530+0000 E QUERY    [js] ReferenceError: dn is not defined :
        @(shell):1:1
        > db.info.find();
        { "_id" : ObjectId("5cd640ef14ccf5417f4bb908"), "name" : "Jack", "role" : "root" }

        2, 创建对特定数据库，比如demo，有读写权限的用户
                db.createUser({user:"test",pwd:"123456",
                                        roles:[{role:"read", db: "user_test" }]) 
        3，数据库的建立
                use user_test;
        4, mongo是否正常启动的校验，
                # 写入一条数据
                db.info.save({name:'test',age:'22'})
                # 查询数据
                db.info.find();
                # 结果，
                { "_id" : ObjectId("5c973b81de96d4661a1c1831"), "name" : "test", "age" : "22" }        
        
        5，远程开启连接. #必须联网
                mongodb容器中
                # 更新源
                apt-get update                   # ubuntu 更新22个包，大约3分钟，16m
                # 安装vim        
                apt-get install vim            # 大约60m，大约2分钟
                # 修改mongo配置文件
                vim /etc/mongod.conf.orig
                bindIp:127.0.0.1 注释掉或修改为0.0.0.0

# 9, 常用指令
        show dbs；                 #查看数据库列表名称
        show collections;         #查看连接用户
         
