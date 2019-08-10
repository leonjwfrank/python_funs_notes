
#    python27 与python36十大差异--基础篇
- 大氵度
----


![Python](https://www.python.org/static/img/python-logo.png)

众所周知python3对于python2有较大改变，这篇文章记录了一些常用的两个版本python27 和python36 之间基础的明显的差别。

##   一        字符编码
###    1.1 python27 允许使用Unicode，utf-8两种编码的string
所以在python27的程式模块中一般首先会有如下声明：
           coding:utf-8

###    1.2 python3统一使用Unicode编码的string
python3中需要保存到硬盘或传输时就转换为utf-8编码，反之亦然，从文本中读取utf-8字符转换为Unicode字符到内存里。
在python36 中encode 和decode 所做的事情如下 

   encode  str --> bytes
   bytes 字符类似于： b’1’
>>> 'a'.encode()
         b’a’
>>>b'a'.decode()
         ‘a’


如果我们从网络或硬盘读取字节流读到的数据就是bytes，这时 
用decode改为str（字符串），然后对其进行len(), join(),write()等操作。
  e = ’数据’.encode()      str 转为 bytes
if isinstance(e, bytes): 
         ue = e.decode(‘utf-8’)          bytes 转为 str, 否则写入失败
with open(‘./test.txt’,  ‘w’) as f:
         f.write(ue)                       


###    1.3 扩展 bytes类型在python3中引入，与C 和2.x类型对照表
+--------------+-------------+------------+--------------------------+
|      C name | 2.x    repr | 3.x repr |
| --- | --- | --- |
|      PyUnicode | unicode u'' | str                   '' |
|      PyString | str      '' | bytes                b'' |
|      PyBytes | N/A | bytearray bytearray(b'') |
|      PyBuffer | buffer | N/A |
|      PyMemoryView | N/A | memoryview         <...> |
+--------------+-------------+------------+--------------------------+



##    二        print语句

###    2.1 语法转变，由语句变为函数； 
```python
  python27 以下语法均正确，有多种用法:  
print  ‘this is debuging’ 
print(‘this is debuging’) 
  python36 仅支持以下函数式用法： 
print(‘this is debuting’) 


###    2.2 更新一，不同的指定显示方式
包括如输出错误方式 ，如果要指定调试输出对象，在python27中用法如下：
```python
python27:    print >> sys.stderr, "error"    

在python36中用法如下：
```python
python36:    print("error", file=sys.stderr)


###    2.3  更新二, 更多样的调用参数
在python36中可以使用新的方式调用模块中的参数值到调试语句
如：
```python
a = ‘develop’
print(f'a value {a}')
a value develop



##    三        单整数类型

###    3.1 int， 在python36中没有long类型 
```python
>>> long(123) 
Traceback (most recent call last): 
File "<pyshell 4>", line 1, in <module> 
long(123) 
NameError: name 'long' is not defined 
>>> int(123) 

###    python27的long 123 
在python27 中long(123) 返回 123L 



##    四        除法规则 

###    4.1 真除法和小数除

比如在python27中 1/2 结果返回0， 在python36中返回0.5，因为： 

/  可能发生整数除法
如果除数和被除数有一个是浮点数 
会发生 （true divison）

   1/2              返回0      这个应该算是个bug，中v3中解决了
   1/2.0       返回 0.5
在python27中  
```python
from future import division

   1/2            返回0.5

   1//2               返回0
   1.0//2.0   返回0.0 

###    4.2 v3 版本 5 / 2 == 2.5而不是2; int值之间的所有除法都会返回浮点数 . 

在v3 版本中的任意两个数字操作数，
/ 将小数除，总是返回浮点数      
          1/2         返回 0.5
          1.0/2.0   返回 0.5  

// 双斜线除法运算号 无论操作数是什么类型，永远表示整数除法  
         1//2                 返回 0
         1.0//2.0     返回 0.0  
```python
    python27 中
>>> 2/4
0
          python36 中
>>> 2/4
0.5


##    五        表示方式 .  

###    5.1 二，八，十六进制 . 

  必须对应
（0b0110， 0o0110， 0x0110） 
36版本和27版本二进制相同表示：
>>>0b0110 
6 
八进制表示方式相同：
>>> 0o0110 
72 
十六进制表示方法相同：
>>> 0x0110 
272 


###    5.2 v3 版本去除0110 .  

python3中直接以 0110 表示，控制台交互器报错非法token
         >>> 0110 
         SyntaxError: invalid token 
这种python27才有的方法 
>>> 0110 
72 

##    六   数值类型操作      

###    6.1 八进制表示方法不同   

```python
  python36 中  c.oct(self) 表示 
>>> oct(6) 
'0o6' 
python27 
>>> oct(6) 
'06' 


c.hex(self) 表示 十六进制 表示方法相同 

###    6.2 python36移除 强制转换为相同的数值类型 函数  coerce .  

```python
coerce(6,10.0) 
Traceback (most recent call last): 
File "<pyshell 31>", line 1, in <module> 
coerce(6,10.0) 
NameError: name 'coerce' is not defined 

> python27 正常使用  ， int类型 6 将被转换为 浮点类型
```python
coerce(6， 10.0)  
（6.0， 10.0） 


##    七        类的定义 .  

###    7.1 在python27中，有经典类和新式类之分 .  

```python
class A:                       经典类
         a = ‘a1’
class Aa():                             经典类
         a = ‘a2’
class Aaa(object):       新式类
         a = ‘aaa’


###    7.2 在 python36中，默认定义新式类    

```python
class Aa:                          新式类
     pass
class A(object):         新式类
         a = ‘a’


###    7.3  如下定义3个类和多重继承关系 .  

经典类多继承属性搜索顺序: 先深入继承树左侧，再返回，开始找右侧;新式类多继承属性搜索顺序: 先水平搜索，然后再向上移动
新式类有新增方法 \getattribute
```python
   inhert_class.py
a():
         def init(self):
                 pass
         def sa(self):
                 print("This is class A")
class B(Aa):
         pass
class C(Aa):
         def sa(self):
                 print("This is class C")
class D(B,C):
         pass
if name == 'main':
         fd = D()
         fd.sa()

      以上代码执行，在python2.7中
        python       inhert_class.py
                This is class A
      python3        inhert_class.py
           This is  class C


##    八        异常捕获 .   

###    8.1 python36版本中异常的捕获 .   

需要as, 同时捕获多种异常需要圆括号 
try:
                        raise AssertionError('error info')
except AssertionError as e:
                   print('error {}'.format(e))
   多种
except (AssertionError, BaseError) as e:
         ...


###    8.2 python27中 逗号 , 隔开    


try:
                        raise AssertionError('error info')
except AssertionError, e:
                   print('error {}'.format(e))
   多种捕获
except (AssertionError, BaseError), e：
         ...


##    九        输入     

###    9.1  python27 Input   raw_input   输入  字符都处理为字符串    

input 输入数字可成功处理为数字。 
```python
>>> input() 
123         输入 
123           输出 
>>> raw_input() 
123          输入 
'123'          输出 

###    9.2. 在python3.x中，整合了2.7.x中的 raw_input 和 input，统一    

input, 输入字符串和数字都处理为字符串。 
```python
>>> input() 
123 
'123' 
>>> input() 
"add" 
'"add" 


##    十        方法变更 .  

###    10.1  dict类型已经重新实现 .   

类似于PyPy dict实现，dict 字典移除方法has_key等,相比旧的版本(python35及以前) ，字典使用的内存减少了20％到25％
在python2.7中判断一个字典对象是否含有某个key可使用如下方法

```python
dict.has_key(‘key’)        
  >>> d2.has_key('a')
True
>>> ’a’ in d2
True

python36中直接使用
```python
         >>> d1.has_key(‘a’)
         Traceback (most recent call last):
         d1.has_key('a')
         AttributeError: 'dict' object has no attribute 'has_key'
         >>> ’a’ in d2
         True 
         
         
         
###    10.2  字典方法 .   

keys()、values()、items()，zip()，map()，filter()
不再默认返回一个list，需要使用list转换。
同时python3 移除iteritems ，
在python2.7 中dict.iteritems是返回生成器， dict.items是返回list,Python2 items（）构建了一个真实的元组列表并返回了它。这可能会占用大量额外的内存。
在python3 中dict.items 返回生成器，没有方法直接返回list，节省了内存，如果需要把生成器转换为list即可。
 

###    10.3   xrange 废弃，range性能优化.    

###    10.4.  迭代对象 .   

值查看方式 iter.next(), 修改为 next(iter)。

###    10.5.  exec 语句 .   

类似于print，修改为函数exec(file.read()), 同
时execfile语句废弃。

###    10.6,  dict 改变 .   

        dict 的取值方式，itervalues   iteritems 在 python3 中分别是 d.values(),  d.items()


## 更新点 .   

        1，新型的 单类类型，类是类对象，实例是实例对象， 名称相同的 类变量 和 实例变量可同时 赋值 和取值；
        2，而在java中，类是类型，实例是类的对象；
        3，单整数类型，int， 在python3中没有long类型
        4，除法：
            / 整数向下除法，如果除数和被除数有一个是浮点数，真除法会发生 （true divison）  1/2 返回0 ， 1.0//2.0 返回0.5
                在v3 版本中的任意两个数字操作数， / 将总是返回浮点数       1/2 返回 0.5，  1.0/2.0 返回0.5

                // 双斜线除法运算号 无论操作数是什么类型，永远表示向下除法  1//2 返回 0，  1.0//2.0  返回 0.0

        5， 在v3中 二，八，十六进制 必须对应（0b0110， 0o0110， 0x0110） ，去除0110 这种表示
            数值类型        c.__oct__(self) 表示 八进制， c.__hex__(self) 表示 十六进制
        强制转换为相同的数值类型  c.__coerce__(self, num)

        6， 内存中大型列表时，可使用迭代器替换，避免内存浪费，如map， filter，range，zip， dict.keys(), dict.value(), dict.items() 每一个都返回迭代器，
            更方便查看数据和资源消耗
        7， v3版本中异常的捕获需要圆括号（）  except（ValueError， IndexError） as e：

                  特别函数：
                           Class.__init__(self, [,arg1...)  构造函数在类实例化时初始化
                           Class.__new__(self, [,arg1...)  构造函数附带任何可选函数，通常用于创建不可变数据类型子类， 实现单例类.
                 模式可实现方法：
                         使用模块     *.pyc唯一，每一个模块都是唯一的
                        使用 __new__    　类的实例和一个类变量 _instance 关联起来，如果为None，创建新的实例，否则返回cls.instance
                        class sign_class(object):
                        """every time instance class is same one"""
                        def __new__(cls, name, age):
                                if not hasattr(cls, "instance"):
                                        cls.instance = super(sign_class, cls).__new__(cls)
                                cls.gender = "male"
                                return cls.instance

                        def __init__(self, name, age):
                        self.name=name
                                self.age=age
                p_jack = sign_class(name="jack", age=101)
                        p_lisa = sign_class(name="lisa", age=91)
                                for obj in [p_lisa, p_jack]:
                                        obj_dic = {}
                                        for n in ["name", "age", "gender"]:
                                obj_dic[n] = getattr(obj, n)
                        print(obj_dic)
                        print(obj.__dict__)     注意gender 是在new中定义的，所以__dict__中并不包含
                {'gender': 'male', 'age': 91, 'name': 'lisa'}
                {'age': 91, 'name': 'lisa'}
        {'gender': 'male', 'age': 91, 'name': 'lisa'}
                {'age': 91, 'name': 'lisa'}
                使用装饰器（decorator）
            from functools import wraps
                def singleton(cls):
                        instances = {}
                        @wraps(cls)
                        def getinstance(*args, **kw):
                                if cls not in instances:
                                        instances[cls] = cls(*args, **kw)
                                return instances[cls]
                        return getinstance

                @singleton
                class B(object):
                    b = 2
                使用元类（metaclass）/py v3

