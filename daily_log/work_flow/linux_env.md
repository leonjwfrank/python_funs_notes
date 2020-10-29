# ubuntu
    # 步骤 修改root密码
    su -    # 切换为root
    passwd   # 设置密码
    su -     # 退出root并测试你设置的密码
    # 禁用root
    sudo passwd -dl root
## ubuntu 创建，修改用户
    sudo adduser kukeg
    添加用户到组 add user tom to multiple groups – foo, bar, and ftp
    useradd -G foo,bar,ftp tom

    usermod命令将现有用户jerry添加到ftp 组使用-a选项
    usermod -a -G ftp jerry
    id jerry
    修改用户jerry的组到 www
    usermod -g www jerry

    查看用户信息
    id jerry
    
# 0,树的目录查看方式
	pstree   # 不跟进程号的时候，树形显示当前目录结构
		pstree -H 88   #树形显示某一进程目录结构
		init---Xvnc
		      -acpid
		      -atd
		      -2*[sendmail]

#1,后台进程维持方式
	nohup/setsid  临时添加后台允许进程方便方法
		nohup ping 127.0.0.1 & #将忽略bash的HUP信号，标准输出和错误将重定向到nohup.out
		setsid ping 127.0.0.1 &  # 创建一个不属于当前bash的进程来执行命令 &表示后台运行
    disown  事后补救当前以及运行的作业，保持后台运行，使用命令jobs不能查看到。 ps -ef可以查看到
    	disown   -h  jobspec  # 使某个作业忽略HUP信号
    		disown -h  %1
    	disown   -ah    # 来使所有作业都忽略HUP信号
    	disown   -rh    #使在运行的作业忽略HUP信号
    screen 在大批量操作时的好的选择
    	screen -dmS session name  坚毅一个端口模式会话
    	screen -list 列出所有会话
    	screen -r session name  重新连接制定会话
    	CTRL -a d 来暂时断开当前会话

    	在bash ping 127.0.0.1
    	不用screen， bash时 sshd的子进程，ssh断开连接时 HUB信号影响该ssh所有子进程
    	使用screen， 此时 bash时screen子进程，而screen时init子进程

    	# 例子
    	screen -r Urumchi
    	ping 127.0.0.1

#2，服务后台维持举例
	nohup /data/name/game/bin/python3 -u /data/name/game/server.py >./log/0108.out 2>&1 &
	nohup /data/name/game/bin/python3 -u /data/name/game/logger.py >./log/0108-logout 2>&1 &

#3, 查询进程所有者信息
	sudo netstat -tupa | grep 8878


# windows
    1.最小化除活动窗口以外的所有窗口
        鼠标选中窗口快速摇晃三次

    2，另一个开始菜单
        win + x

    3，截图
        1，全屏，prtSc
        2，Windows键+ Shift + S打开一个名为Snip＆Sketch的工具，使用该工具可以单击并拖动以创建屏幕截图，并将其保存到剪贴板。
    4，快速启动任务
        Windows键+ [数字键]，数字键与程序在任务栏上的位置相对应。例如，Windows键+ 2将打开任务栏上的第二项。
    5，关闭windows广告
        “设置”>“个性化”>“开始”。在“开始”位置将名为“偶尔显示建议”的设置切换到关闭位置
    6，关闭后台应用
        设置-后台应用
    7，非活动窗口打开 鼠标滚动功能
        请转到“设置”>“设备”>“鼠标”，然后将“将非活动窗口滚动到”上时将其切换为“打开”
    8，解决VM虚拟化不能与hyper-V 或Device共用的问题
        在控制面版-程序-启用/关闭windows功能中 关闭hyper-V所有功能，关闭Contents  
            或 在管理员权限下执行bcdedit /set hypervisorlaunchtype off
        win+r运行中输入：msinfo32，回车，打开系统信息
        修改注册表
        你会发现基于虚拟化的安全性还是处于运行状态，Device/Credential Guard 这样是不行的。下面说说如何将它关闭：
        下面的操作非常重要 

        1.win+r运行→输入：regedit→打开注册表编辑器

        2.在地址栏粘贴复制（或者一个个文件夹点击进入）：计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard
        如下步骤：
            \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard
            修改或新增4项内容，分别为：
            ConfigureSystemGuardLaunch值为2
            EnableVirtualizationBasedSecurity值为0
            RequireMicrosoftSignedBootChain值为1
            RequirePlatformSecurityFeatures值为1
            名字不能错，从上面粘贴复制，新建项都为DWORD(32位)，关于这4项的 官方说明 https://docs.microsoft.com/zh-cn/windows/client-management/mdm/policy-csp-deviceguard

            \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa
            新增1项内容，如下：
            LsaCfgFlags值为0
            名字不能错，从上面粘贴复制，新建项为DWORD(32位) https://docs.microsoft.com/zh-cn/windows-hardware/customize/desktop/unattend/microsoft-windows-deviceguard-unattend-lsacfgflags
        3， 重启后 VM即可运行