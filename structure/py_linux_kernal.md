# linux kernal
##	1 内核I/O:
		内核--进程
		进程描述符：进程元数据  双向链表
		linux抢占
		系统时钟：时钟
		tick：滴答 时间解析度，100Hz，1000Hz   1秒计数1000次
		时钟中断
		进程交互类别：
		交互式进程（I/O）
		批处理进程（CPU）
		实时进程（Real-time）
		
		CPU：时间片长，优先级低
		IO：时间片短，优先级高
##  2 linux优先级:priority
		实时优先级：1-99，数字越小，优先级越低
		静态优先级：100-139 ，数据越小，优先级越高	
		实时优先级比静态优先级高
		:duref:`ref <ps -e -o class,rtprio,pri,nice,cmd）>`
	    ps -e -o class,rtprio,pri,nice,cmd   
			-e 所有与终端有关无关的进程信息
			-o 自定义显示 
			class 调度类别
			rtprio 运行实时优先级
			pri 进程优先级
			nice 调整静态优先级   -20，19 ：100，139  nice值为0对应为优先级 120

###     2.1 调度类别： 按优先级进行调度 
		实时进程：
			SCHED_FIFO:First in first out    上图中调度类别CLASS中的 FF
			SCHED_RR:Round Robin
			SCHED_Other:调度100-139之间的进程   上图中调度类别CLASS中的 TS
			http://honglus.blogspot.com/2011/03/understanding-cpu-scheduling-priority.html
###     2.2 动态优先级算法
        :duref:`ref <dynamic priority=max（100，min（static priority - bonus +5，139））>`
		dynamic priority=max（100，min（static priority - bonus +5，139））
		bouns  奖惩措施 范围 0-10
		110，-3
		110-(-3)+5 =118 
###	    2.3 手动调整优先级
		100-139：nice
		nice N   COMMAND
		renice -n # PID
		chrt -p [prio] PID
		1-99：
		chrt -f -p [prio] PID
		chrt -r -p [prio] PID
		chrt -f -p [prio] COMMAND
		ps -e -o class,rtprio,pri,nice,cmd   
		(o1) 调度无论有多少进程，调度列表只有139个列表等等扫描
		CFQ Complete Fair Queue 完全公平调度 适合桌面系统
		SCHED_Other
	

##  3 linux进程创建机制
		COW
		Kernel -->init
		init
		fork():
		task_struct
		Memory-->Parent
		COW:Copy On Write
		prefork
##  4 OS system
		cpu <----> NorthBridge <----->RAM
		单进程最大3G使用内存
		32位，64位 cpu 寻址 2^32=4G , 
		PAE  物理地址扩展 32bits+4bits  64G
		存取速度，CPU寄存器 > 一级缓存>二级缓存>三级缓存>RAM内存>硬盘
		N路关联    Interrupt Controller
		内存RAM  BIOS DMA 
		4k，page，page frame（页框）
		计算机 核心三部分：运算器，控制器，存储器       显卡为   IO设备
		tcp 端口号其实就是进程地址
		程序 局部性，空间局部性，时间局部性