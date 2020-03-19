## 一， 数据库的连接
        1， sqlite 过于小型，在docker中使用不佳

        2， 使用pymysql， mysql 连接，总是有错误
                sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1045, "Access denied for user 'fwk'@'172.17.0.1' (using password: NO)")
        
        3， 使用mongodb， FLASK-PyMongo 库查询结果错误，非mongo或python标准库

        4， 使用docker，docker build 总会有venv 权限问题

        5，从sqllite改为mysql 只需要修改配置.env 中，FLASK_CONFIG=default 改为 FLASK_CONFIG=docker

## 二， 部署mysql
        添加源
        $wget 'https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm'
        $sudo rpm -Uvh mysql57-community-release-el7-11.noarch.rpm
        $yum repolist all | grep mysql

        mysql-connectors-community/x86_64 MySQL Connectors Community                  36
        mysql-tools-community/x86_64      MySQL Tools Community                       47
        mysql57-community/x86_64          MySQL 5.7 Community Server 
        安装最新版
                        $sudo yum install mysql-community-server

        启动mysql服务
                          $sudo service mysqld start
        $sudo systemctl start mysqld #CentOS 7
        $sudo systemctl status mysqld 


        修改默认编码
                vim /etc/my.cnf
        修改默认密码
                查看 /var/log/mysqld.log 生成默认密码    <f?uu?pil5BO
                登陆：mysql -uroot -p
                mysql>ALTER USER USER() IDENTIFIED BY '1qaz%WSXroot';
                修改策略为1，长度为4
                  set global validate_password_length=1;
                                                mysql> select @@validate_password_length;
    +----------------------------+
    | @@validate_password_length |
    +----------------------------+
    |                          4 |
    +----------------------------+

        # 修改为 简单密码
        ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
        # 或  
        ALTER USER USER() IDENTIFIED BY 'root';

        # 策略
                mysql> SHOW VARIABLES LIKE 'validate_password%';
    +--------------------------------------+-------+
    | Variable_name                        | Value |
    +--------------------------------------+-------+
    | validate_password_check_user_name    | OFF   |
    | validate_password_dictionary_file    |       |
    | validate_password_length             | 4     |
    | validate_password_mixed_case_count   | 1     |
    | validate_password_number_count       | 1     |
    | validate_password_policy             | LOW   |
    | validate_password_special_char_count | 1     |
    +--------------------------------------+-------+
    7 rows in set (0.01 sec)


# 三，创建和授权用户
        # 如果是docker 容器的mysql先执行: docker exec -it mysql bash
        mysql -uroot -p
        
        #本地登陆
        mysql>CREATE USER 'innsowl'@'localhost' IDENTIFIED BY 'innsowl';  
        #远程登陆
        mysql>CREATE USER 'innsowl'@'%' IDENTIFIED BY 'innsowl';       
        
        # 创建表
        create database testDB default charset utf8;

        # 授权用户对数据库对权限
        grant all privileges on testDB.* to innsowl@localhost identified by 'innsowl';
        
        # 授权所有数据库部分权限
        grant select,delete,update,create,drop on *.* to test@"%" identified by "1234";

        # 删除用户
        Delete FROM user Where User='test' and Host='localhost';
        
        # 修改用户密码
        mysql>update mysql.user set password=password('新密码') where User="innsowl" and Host="localhost";
        mysql>flush privileges;        

#四，数据库操作
        # 创建db
        create database testDB default charset utf8 collate utf8_general_ci;
        # 表结构
        describe  innsowl;            
        # 删除数据库和表
        drop  database  db;
        drop table  tablename;

# 五，表操作
        CREATE TABLE IF NOT EXISTS `image`(
        `id` INT UNSIGNED AUTO_INCREMENT,
        `image_filename` VARCHAR(100) NOT NULL,
        `image_url` VARCHAR(40) NOT NULL,
        `image_string` VARCHAR(40),
         PRIMARY KEY ( `image_filename` )
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;

        添加字段：
                ALTER TABLE posts ADD status INT AFTER body_html;
        设置默认值：
                ALTER TABLE posts ALTER status SET DEFAULT 1;
        修改字段：
                ALTER TABLE testalter_tbl MODIFY c CHAR(10);


    参考
        https://www.cnblogs.com/ivictor/p/5142809.html
        https://www.jianshu.com/p/da28ec28ef4b
        
# 1, docker image 目录
         所有images信息所在文件，/var/lib/docker/image/overlay2/repositories.json
         目录名即为该镜像的Image ID
         首先是metadata目录，该目录保存每个镜像的parent镜像ID，因为这里的alpine:lasted镜像没有更上层的镜像，所以目录为空，后续我们使用docker build构建一个镜像，再进一步分析。

         其次是content目录，该目录下存储了镜像的JSON格式描述信息：
         解释以下主要的几个部分：

         config: 未来根据这个image启动container时，config里面的配置就是运行container时的默认参数。
         container: 此处为一个容器ID，一般我们执行docker build构建镜像时，可以看见是不断地生成新的container，然后提交为新的image，此处的容器ID即生成该镜像时临时容器的ID，后面通过docker build构建镜像会进一步验证。
         container_config：上述临时容器的配置，可以对比containner_config与config的内容，字段完全一致，验证了config的作用。
         history：构建该镜像的所有历史命令
         rootfs：该镜像包含的layer层的diff id。
        还是OCI Image的原理所致，最需要记住的是每一个Layer记录的是与上一层Layer相比的变化。
        OCI映像是根文件系统更改的有序集合以及在容器运行时内使用的相应执行参数。此规范概述了描述用于容器运行时和执行工具的图像的JSON格式及其与文件系统更改集的关系，如图层中所述。

# 如下，本地image创建后没有推送到远程，所有digest为NONE

    docker images --digests        
    REPOSITORY           TAG                 DIGEST                                                                    IMAGE ID            CREATED             SIZE
    innsowl              515site             <none>                                                                    2870a8eec2d2        9 hours ago         140MB
    mongo                3.2                 <none>                                                                    94c2dc879674        5 days ago          302MB
    innsowl              510webs             <none>                                                                    d2eeb27cf80d        5 days ago          140MB
    mysql                latest              sha256:711df5b93720801b3a727864aba18c2ae46c07f9fe33d5ce9c1f5cbc2c035101   990386cbd5c0        5 days ago          443MB
    debian               jessie-slim         sha256:26e0cdb965642bb867ba565316cf8d50c1d782574b54d46f06ea7b90039fc7b5   dc5ba56066bd        7 days ago          81.4MB
    mongo                latest              sha256:02c6031b363fb9a43f6633eb9db405db59c9dfdd0ce726baa4fab973939952a4   d98005b752b4        8 days ago          411MB
    innsowl              51jobs              <none>                                                                    8d7e57f4ab00        12 days ago         139MB
    innsowl              51work              <none>                                                                    8d7e57f4ab00        12 days ago         139MB
    mysql/mysql-server   5.7                 sha256:ddb046076781a15200d36cb01f8f512431c3481bedebd5e92646d8c617ae212c   857eadf53a54        2 weeks ago         258MB
    mysql/mysql-server   latest              sha256:8dd16a45d0e3e789f2006b608abb1bb69f1a8632a338eef89aec8d6fccda7793   39649194a7e7        2 weeks ago         289MB
    python               3.6-alpine          sha256:8f9fa29cd9d2e1c8b762ddfecc4871fe5a3e8444ec3a2b57d2b6f2a172c4cd50   148efb059c7f        5 weeks ago         79.1MB
    hello-world          latest              sha256:92695bc579f31df7a63da6922075d0666e565ceccad16b59c3374d2cf4e8e50e   fce289e99eb9        4 months ago        1.84kB

        
        