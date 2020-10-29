# 判断时间点当前是否零点
	time.time()%86400 == 3600*(-8+24)


# py在 centos安装问题
	1,下载并进入解压源码包
	./configure --prefix=/usr/local/python3   # prefix 指定安装位置
	make & make install

	2，添加py3版本文件连接
	ln -s /usr/local/python3/bin/python3 /usr/bin/python3

	3,验证 python3 -V

	4,python3 -m pip -V 报错则配置php
	ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

# centos的pycurl安装问题或pycurl导入错误问题
	注意两点
	@1，python3-devel 与python-devel不同
	@2，yum安装需要权限，yum安装可能有冲突，要解决冲突。

	>>>import pycurl
	ImportError:pycurl:libcurl link-time ssl backend(nss) is different from compile-time ssl backend(openssl)
	或
	ImportError:pycurl:libcurl link-time ssl backend(nss) is diffeerent from compole-time ssl backend(none/other)

	解决：
	1，先安装 curl
	wget http://curl:haxx.se/download/curl-7.43.0.tar.gz
	解压 tar -zxvf
	编译及安装
	./configure
	make && make install

	2，centos 需要安装gcc编译包 python-devel 3.6
	sudo yum install python3-devel --nodeps   # nodeps 无依赖安装python3-devel开发工具，但是不安装依赖将报错，因为python3开发工具并没有安装

	sudo yum install python3-deval 安装有报错是 epel-release-6.8.noarch的版本冲突
	file /etc/rpm/macros.ghc-srpm from install of rehat-rpm-config-9.1.0-88.el7.centos.noarch conflicte with file from ...

	3，解决epel-release冲突
	sudo yum erase epel-release
	继续安装
	sudo yum install python3-devel.x86_64
	安装成功

	4，安装pycurl
	pip3 install pycurl    #安装成功，但是还不能用，需要卸载重新安装，这次不用安装编译包。
	## 卸载pycrul，
	pip3 uninstall pycurl
	## 不带缓存的安装
	export PYCURL_SSL_LIBRARY = nss    #NetWork Security Services
	pip3 install pycurl --no-cache-dir  #--no-cache-dir   # 不缓存
	或
	export PYCURL_SSL_LIBRARY=openssl
	pip3 install pycurl --no-cache-dir   # --no-cache-dir #不缓存
	完成

	gcc -I/usr/include/python2.7 pycurl.h -o program
	pycurl.h 编译失败，需要重新编译。指定gcc编译目录，需要Python.h文件路径。



