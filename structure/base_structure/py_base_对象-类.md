h2. 1, 编程方法
	h3. 面向过程
      语言代表:c, c++
	h3. 面向对象
      语言代表:c++, java, python
	h3. 函数式
      语言代表:FORTHAN, python
	h3. 汇编
      语言代表:机器码, Basic

h2. 2, 基本步骤
	h3. 分析对象
		特征
			姓名,年纪,性别,职业...
		行为
			跑步,速度
	h3. 写代码表现对象
	h3. 实例化对象
h2. 3, 基本概念
    h2.  #OOP(Object Oriented Programming)
    h2. 核心思想
        抽象对象(Object)
        归为类(Class)
    h2. 设计思想
        抽象出Class
        根据Class创建instance
        类 是对象的定义
        实例是真正的实物
    h2. 三大特点
        数据封装
        继承
        多态
    h2. 主要目的
        提高程序的重复使用
    h2.  #面向对象vs面向过程
       h2. 面向对象分类
           面向对象把对象作为程序的基本单元
           一个对象包含数据和操作数据的函数
       h2. 面向对象特点
           一组包含对象的集合
           每个对象都可以 接收/处理 其他对象的小心
       h2. 面向过程:依次执行
           面向过程特点:一组命令的集合,一组函数的程序顺序执行
           把大块函数分解成小块函数,降低系统的复杂度
    h2.  #类变量&实例变量
       h2. 类变量
           定义 在类中且在函数体之外

           特点 
               在这个类的所有[实例]之间共享
               清理不作为实例变量的使用
           访问
               内部类 or 外部类
               className,classValue
       h2. 实例变量
           定义在[方法]中
           只作用与当前实例的类
    h2. # 数据成员
        类变量, 实例变量, 用于处理 类及实例对象相关的数据
        方法 类中定义的函数
h2. 4, 结构
    h2. # 基本结构
       h2.  class 创建类的过程 
            ClassName#类名大写开头的单词
            bases 一或多个,用于继承父类的集合
            object 本身,所有类最终都会继承的类
            class docs string
                class.__doc__ ,类的文档字符串,说明类的基本功能和author等
            class_suite 组成包括:
                类成员
                方法
                数据属性
       h2. 类的特点:
            属性 attribute
                类下定义的变量
                命名 名词
            方法 method
                类下定义的函数
                    实现了数据封装
                    使用时无需知道内部实现细节,直接操作对象类的数据
                举例
                class A(a=None):  
                   a = a  # 类变量
                   attr_feature = True #类属性
                   def A1(): # 类方法
                      print a

    h2. # 类属性
        实现类的步骤
           对象的抽象
           对象的蓝图,模板
           实例
       h2. 分类
           数据属性:添加,删除,修改
           方法:执行调用
       h2. 内置特殊类属性
           ClassName.__name__ 返回类名
               直接执行 __main__
               作为导入模块,导入模块名
           ClassName.__doc__ 类的文档字符串
           ClassName.__bases__ 所有父类的元组
           ClassName.__dict__ 属性
           ClassName.__module__ 类定义所在模块
           ClassName.))class__ 对应的类
      h2. __init__(self,)
          h2.  # 特殊方法  称为具体的初始化方法/构造函数
          h2. # 初始化 创建实例对象时,自动调用,强制绑定属性
          h2. # self 类的实例
                   定义类的方法时,永远的第一个参数, 表示类的实例本身
                   把各种属性 绑定到self
          h2. # 示例:
                class B:
                    empCount = 0
                    def __init__(self,(name, age)):
                        self.name = name
                        self.age = age
                        B.empCount += 1
          h2. 调用过程,通过__init__传递参数
                In [2]: B.empCount
                Out[2]: 0

                In [3]: B1 = B('jack', 35)
                In [4]: B1
                Out[4]: <__main__.B at 0x449def0>
                In [5]: B1.empCount
                Out[5]: 1

                In [6]: B2 = B('Susan', 25)
                In [7]: B2.empCount
                Out[7]: 2

    h2. 访问限制
       h2. 私有变量
            变量名以_开头
            内部属性不能被外部访问
       h2. 私有变量的改变和访问
            h2. 获得内部属性
                增加方法
                    def get_name(self):
                        return self._name
                直接访问 object.className._attrName
            h2. 允许外部代码访问
                增加方法 保证对参数进行检查,避免传入无效参数
       h2. 实例变量 定义在方法中的变量, 只作用于当前实例的类
       h2. 特殊属性
            可以访问 特殊变量      __x__ 
            不能访问 私有变量      __x
            可以访问 不要随便访问  _x
       h2. 类的专有方法

            __init__ : 构造函数，在生成对象时调用
            __del__ : 析构函数，释放对象时使用
            __repr__ : 打印，转换
            __setitem__ : 按照索引赋值
            __getitem__: 按照索引获取值
            __len__: 获得长度
            __cmp__: 比较运算
            __call__: 函数调用
            __add__: 加运算
            __sub__: 减运算
            __mul__: 乘运算
            __div__: 除运算
            __mod__: 求余运算
            __pow__: 乘方
            __str__: str重载函数
	            class people:
				    def __init__(self,name,age):
				        self.name=name
				        self.age=age

				    def __str__(self):
				        return '这个生物的是%s,已经压了%d年了！'%(self.name,self.age)
				#输出
	            In [33]: people('孙猴子', 500)
				Out[33]: <__main__.people instance at 0x00000000042FF3C8>

				In [34]: print people('孙猴子', 500)
				这个生物的是孙猴子,已经压了500年了！


    h2. 对象的性质
       h2. 区分
           类的属性    所有属于该类的对象会共享这些属性
           对象的性质  该对象的特别信息
       h2. 定义方法
           __init__()
               赋值:
                   通过引用 self.attrbute
                   self传递给各个方法
                   对象的性质,查询式修改
           示例:
           class human(object):
               def __init__(self, input_gender):
                   self.gender = input_gender
               def printGender(self):
                   print(self.gender)
    h2. BIF
        h2. 布尔函数 True
            issubClass(sub, sup)
                sub是sup的子类
                如:一个类是其自身的子类
            isinstance(obj, class)
                obj 是class 的一个实例
                可以是多个类的元组 class
                isinstance(1, int)
        h2. *attr()系列
            各种对象,使用范围
            使用方法 *attr(obj, 'attr'...)
            系列BIF
                hasattr(obj,name) 检查属性是否存在          
                getattr(obj, name[,default]) 访问属性                   
                setattr(obj, name,value)  设置一个属性/不存在则新增                       
                delattr(obj, name) 删除属性                     
            dir() 获得一个对象的所有属性和方法 
            super() 获取所有属性(父类)  
            vars() 属性值, 字典 
    h2. 继承与多态
        h2. 继承  子类-->父类/基类
            h2. 方法
                定义时,括号类写要继承的类名
                没有指定,默认继承object
            h2. 目的
                享有的父类的属性, 通过继承,提高代码的重用
            h2. 特点
                基类 __init__()
                    不会自动调用,需要在原生类__init__()专门调用
                调用基类方法
                    加上基类的类名前缀
                    带上self的参数变量
                调用方法查找方式:
                    先在本类中查,查不到就去基类查找
            h2. 多重继承
                定义类时,列了一个以上的类,继承元组
        h2. 多态
            定义一个数据类等于定义个class
            在继承关系中,实例的数据类型 是某个[子类]或[父类]
            对于一个变量,只需知父类型,无需知道子类型
            调用父类方法时, 作用对象的子类型由该对象的确切类型决定
            h2.  h2.  #开放原则
                对扩展开放  父类的子类,允许新建
                对修改封闭  继承父类的元素不需要修改
