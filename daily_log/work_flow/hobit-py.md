# 习惯
## 1, 引用环和深浅拷贝
	def foo(x=[]):
		x append(1)
		print(x)
	>>>foo()
	[1]
	>>>foo()
	[1,1]
	>>>foo()
	[1,1,1]

	def foo(p=None):
		if p is None:
			p = []
		p.append(1)
		print(p)
	foo()
	[1]
	foo([2,3,4])
	[2,3,4,1]

## 1.1模块的循环导入
	# fred.py
	import wilma
	count =4
	def main():
		wilma.pr('Hello')
	if __name__ == '__main__':
		main()
	# wilma.py
	import fired
	def pr(str):
		print(str*fired.count)
	if __name__== '__main__':
		pr("Ok")
## 1.2 基础规则
	@参数 -u unbuffered
	该次执行不缓存sys.stdout,直接输出控制台
	@参数 -m 
	执行时带参数m，以Script方式执行py模块
    @参数 -x
    跳过py模块第一行，允许使用非unix形式
    @参数 -X
    实体具体选项(set implementation-specific option)
    file 
    程序读取文件内容并执行
    @参数 -
    程序从stdin 读取
dd
	python3 --help  # 显示所有参数

# 2, 内存管理
	2.1 小的整数 和短小字符，python将缓存以便重复使用
	is关键字，用于判断两个引用所指对象是否相同
	>>> a = 'gd'
	>>> b = 'gd'
	>>> a is b
	True

	== 只判断值是否相同
	a2 = []
	b2 = []
	>>> a2 is b2
	False
	>>> b2 == a2
	True

## 2.2 对象引用时python基本构成方式
	赋值的本质 a=1，实际上时修改globals()字典的值，局部变量值的修改locals()的访问和修改
	>>> a1
		very good m
    >>> globals()['a1'] = 'bad good mm'
    >>> globals()

## 2.3 引用对象reference count	
	sys.getrefcount() 查看对象的引用计数，sys.getrefcount()在查看某个引用时将创建一个临时引用，所以引用计数将多1
	>>> c=[1,2,3]
	getrefcount(c)  #这里c只有一次引用，但是计数时2，因为当前查询有一次临时引用
	2
	引用计数的减少和增加
	>>> d=c
	getrefcount(c)  # 增加引用d，计数3
	3
	del d #删除引用d，c的引用计数又重新为2

## 2.4 垃圾回收机制 garbage collection
	垃圾回收时py 独占进行的，大大降低py效率，特定条件下自动启动垃圾回收。
	手工回收 gc.collect()
	py 运行时分配对象obj allocation 和取消分配对象 deallocation次数被记录，高于垃圾回收阈值，启动垃圾回收
	gc.get_threshold()查看该阈值，gc.set)threshold()重新设置该阈值
	(700, 10, 10) 700表示启动垃圾回收阈值，10，10表示分别回收的阈值


	2.4.1 垃圾回收分代策略 generation，基本假设如下
		存活时间越久，越不可能在后面程序中变为垃圾。 这样所有对象分为0,1,2三代，所有新建对象都是0代。某一对象经历垃圾回收，仍然存活，那么它就被归入下一代对象。垃圾回收时，一定扫描0代对象，如果0代经过一定次数垃圾回收，下一次对0代和1代扫描清理，当1代也经历一次次数垃圾回收，这启动0，1，2所有对象的扫描
		以上get_threshold()返回（700,10,10）两个表示每10次0代垃圾回收，将配置1次1代垃圾回收，每10次1代垃圾回收，才有1次2代垃圾回收。
	2.4.2 两个对象相互引用，构成引用环 reference cycle，该引用环将给上一节2.4.1的垃圾回收带来困难，引用环可能构成一些无法使用但引用计数不为0的对象
	为了回收该引用环对象，py复制了每个对象的引用计数为 gc_ref 遍历所有对象，将每个对象引用的对象相应的gc_ref减1，遍历结束后，gc_ref不为0的对象和这些对象的引用对象，以及继续更新下游引用对象，被爆了，其他对象被回收。
	# 参考 内存管理，函数默认参数，动态类型

	2.4.3 迭代
		可迭代对象 __iter__
		迭代器 __iter__ + __next__
		生成器 特殊迭代器 yile
		def yd():
			a = 100
			yield a
			yield a*8
			yield 8000
	2.4.4 抽象方法*(函数)
		对象方法(self.对象方法)，类方法(@classmethod),静态方法(@staticmethod)
		抽象方法 需要子类实现的方法 用@abc.abstractmethod以及 __metaclass__ = abc.ABCMeta 使得任何继承自父类的子类必须覆盖实现抽象方法，否则抛出异常
# 3，其他概念
	闭包  closure
	闭包指的是 难以读取其他函数内部遍历的函数
	实现： 定义在函数内的内部函数可以读取外层函数变量，从而实现闭包
# 4，惯例;
		1,判定dict的key是否存在，使用key in dict而不用 has_key
		2,not的位置，使用key not in dict 而不用 no key in dict
		3, 使用 dict.get(key[,default])如果key存在，返回，否则返回default
		4, 数组字典初始化
			dic = {}
			for k,v in data:
				group = dic.setdefault(key,[])  #如果存在，返回dic[key],不存在把dic[key]设为defalut并返回
			    group.append(v)
			from collections import defaultdic
			    dic = defalutdic(list)
			    for (k,v) in data:
			    	dic[key].append(v)  #所有key都有一个默认值
	迭代一个数组，使用for i,e in enumerate(array) 而不是 for i in range(len(array))
	enumerate 还有第二个参数
	    5，py3元组unpack
	    first, second,*rest, last = range(10)
	    0	1	2~8		9
	    6, 函数参数传入
	    def foo(x,y):
	    	print(x,y)
	    adict = {'x':1, 'y':2}
	    foo(**adict)   #字典key作为参数名传入参数值
	    alist=[1,2]
	    foo(*alist)

	    7, 字符串连接
	    name = "Wang" "Hone"  # WangHong

	    8, 解释器中的 _
	    上一次接收器的返回值
	    9，嵌套列表推导式
	    [(i,j) for i in range(3) for j in range(i)]
	    10, print重定向
	       print >>open('a.txt', 'w+'), 'hello,world'
	    11,反射
	    	isinstance(obj, class)   #检查是否某个自定的类
4，Picking是Python数据结构的序列化过程
	存储一个对象，稍后再取出读取
	如何pickle 已存在的对象类型到文件
	json = {'name':'jack', 'age':100}
	json_file = open('json pkl', 'rb')
	pickle.dump(json.json_file)
	json_file.dump(json,json_file)
	json_file.close()

	取出
	data=pickle.load(json_file)
	print(data)
	json_file.close()

	pickler内建类型和外部方法
		类自定义行为
		__getinitargs__(self)  #
		__getnewargs__(self)
###		Slate 记住它曾经是什么，以及什么时候赋值给它  ？

# 5，对象模型Python3和Python2.x之间的主要区别
	Python3的string和unicode区别不复存在，因此__unicode__被取消 __bytes__加入进来(与python2.7的__str__和__unicode__行为类似)，用于心的创建字节数组的内建方法

	py3默认除法变成了true除法，因此__div__取消
	__coerce__被取消，因为与其他魔法方法有功能重复
	__cmp__ 取消，与其他魔法方法功能重复
	__nonzero__被重命名为 _bool_
# 6,断点
	6.1， 断点设置后，代码执行到该位置，程序挂起检查程序行为
	6.2， 异常断点，到达断点后要执行的操作
	6.3,  断点属性，达到断点时要执行的操作
		  挂起策略，用于定义在遇到断点时是否必须挂起应用程序
		  对其他断点的依赖，
		  何时必须击中断点
	6.4   消息记录
		断点命中消息，命中断点时，控制输出一条日志消息
		堆栈跟踪 断点的堆栈跟踪将命中打印到控制台

	6.5 断点工具
		pdb 交互式代码调试，功能包括
			设置断点，单步调试，进入函数调试，查看当前代码，查看栈片段，动态改变变量的值
			进入pdb交互界面
		命令
			break 或b设置断点     
			continue 或c   继续执行
			list或l        查看当前代码段
			step或s        进入函数
			return或r      执行代码直到当前函数返回
			exit或q		   中止并退出
			next或n         执行下一行
			pp             打印变量的值



# 7, nginx
	nginx 配置个人目录权限700
	东西放在 /home/htdocs/{name}/{project}
	/home/htdocs/{name}/conf nginx 配置

# 8，依赖问题
	pycurl 需要contos 7安装python3-devel   #完成
	具体过程pycurl-centos7

# 9, 发布流程
	1，编译生成pyc文件，建议增加-O优选项
	python3 -O -m compileall -b .
	2, 删除py文件
	    find . -name "*.py"|xargs rm -rf
	3, 删除__pycache__目录
	    find . -name "__pycache__" |xargs rm -rf
	4, 打包 tar包
	   cd ..
	   tar -cjvf xxx.1.1.00.tar.bz2 xxx
	5, 或git push到仓库
	   git push origin master:master
