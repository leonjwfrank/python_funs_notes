## 3的特性
    1， print变成函数，并且有软空格
    print("A\n","B")    # 注意B 之前有个软空格
    A
     B
    2，字典
    py3 的items，keys，values不会再返回列表,而是返回一个易读的“views”
    
    3, map() 和filter() 将返回iterators，如果需要列表，则使用 list(map(...)), 更推荐的是lambda表达式
    4, zip() 返回一个迭代器
    5, 胡乱的比较是没有意义的,相比较的元素必须是能够比较的才行
        1 < ”,0 > None,len <= len这样的语句不再合法了。None < None也会抛出TypeError异常，而不是返回False
    6, builtin.sorted和list.sort()不再有提供比较函数的cmp参数,只有参数key和reverse
    7, 比较函数 __cmp__ 不推荐了，推荐__lt__,eg__和__hash
    8, int的整型,基本跟之前的long一样
    9, 1/2这样的语句将返回float，即0.5, 而不是python2中的0
    10,字符集格式
        Text Vs. Data 代替 Unicode Vs. 8-bit
        py3  使用文本和二进制代替了Unicode字符串和8-bit字符串，所有文本默认返回unicode编码
        使用str(u'')保存文本，使用bytes(b'')保存数据。
        当混淆文本和数据时，py3抛出TypeError错误
        * str和bytes不能混淆
        使用str.encode()将str转换为bytes，使用bytes.decode()将bytes转换为str.
        也可以使用bytes(s, encoding=…)和str(b, encoding=…)
        str和bytes都是不可变的类型
        
        ** 可变类型的bytearray，可以保存缓存的二进制数据
        能够接受bytes的API都能够使用bytearray。这些可变的API是基于collections.MutableSequence的
        文件默认使用文本类型打开,这也是open()函数
        
        ** 要打开二进制文件必须使用b参数
        系统的LANG设置好,因为关于系统的API，如os.environ和sys.argv,当系统允许bytes并且不能正常转换为unicode，可能出错。
        
        编码 代码默认为UTF-8编码
        加入了io模块,并分别使用io.StringIO和io.BytesIO分别用于text和data
        
    11, 语法
        1，函数注释语法，和 函数变量注释语法
        2，类的注释语法
        3，nonlocal声明。使用nonlocal x可以直接引用一个外部作用域的变量,但不是全局变量
        4，key-only参数变量
            星号可以以一个参数的形式出现在函数声明中的参数列表中，但星号之后的所有参数都必须有关键字（keyword），
            这样在函数调用时，星号*之后的所有参数都必须以keyword=value的形式调用，而不能以位置顺序调用
            def test(a, b, *, name):
                return name * (a + b)
            
            test(1,2, 'jack')  # 报错 Typeerror  2 positional arguments but 3 were given
            test(1,2, name='jack')  # 正确 返回 'jackjackjack'
         5，推导: 字典，集合， 列表都可以推导 # 详见 本包的 字典的笔记模块
         
         6， 参数是可迭代对象，可以按位置解包
         def foo(a, b_c):
	        b, c = b_c
	        return b + c
	     7，移除<>,使用!=代替
	     8，exec()不再支持流变量,如exec(f)需写成exec(f.read())
	     9，导入
	        所有不以.开始的import语句均作为绝对路径的import对待
## 31～34的特性
    1, 字典的遍历
    常规Python字典以任意顺序遍历键/值对。多年来，许多作者编写了替代实现，这些实现记住了最初插入密钥的顺序	
    
    2, 千分位分割符
        format(1234567, ',d')
        '1,234,567'  
        
        format(1234567.89, ',.3f')
        '1,234,567.890' 
        
    3, 精度的处理
        from decimal import Decimal
        format(1234567.89, ',f')
	  
            '1,234,567.890000'
        format(Decimal('1234567.89'), ',f')
	  
            '1,234,567.89'
    4,  数据的二进制位数
            (2**123).bit_length()   # 124位二进制
            124
        数据的十进制位数            # 38位十进制，其实是转换为字符串的长度
            len(format(2**123, 'd'))
    5, with上下文管理，同时打开两个文档，一个读数据，一个写数据
        with open('mylog.txt') as infile, open('a.out', 'w') as outfile:
         for line in infile:
             if '<critical>' in line:
                 outfile.write(line)
                 
    6，自动计数，一个可迭代对象中，统计每个元素出现几次
        collections.Counter([1,1,2,3,4])
	        Counter({1: 2, 2: 1, 3: 1, 4: 1})           
    7，itertools.compress(data,selectors)   # 在data中选择 符合 selectors真值测试的元素
        def compress(data, selectors):
            # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
            return (d for d, s in zip(data, selectors) if s)
    
        list(compress("ABCEDFG",[1,1,1,0,1,1,0]))
	        ['A', 'B', 'C', 'D', 'F']
	8, itertools 扩展集 more-itertools
	    pip install more-itertools  # python36 默认已经有了
	    
## 36的特性

### 格式化的字符串文字
    PEP 498, formatted string literals.
    示例:
        旧
        "%s-%d"%('a', 1)
        "{}-{}".format('a', 1)
        新
         a='a'
         b=1
         print(f"{a}-{b}")

### 以数字文字表示
    PEP 515, underscores in numeric literals.
    数字增强，增加了在数字文字中使用下划线的能力，以提高可读性
    1_000_000_000_000_000
    0x_FF_FF_FF_FF
    
    允许在数字之间和任何基本说明符之后使用单个下划线。不允许一行中的前导，尾随或多个下划线。
    该字符串格式化语言现在也拥有了支持’_’信号为千位分隔符使用下划线的浮点呈现类型和整数呈现类型选项’d’。对于整数呈现类型’b’， ‘o’，’x’，和’X’，下划线将被插入每4个位数：
    "{:_}".format(0xf000000)
        '251_658_240'
    "{:_}".format(10000000)
        '10_000_000'
        
    
### 变量/函数注释的语法
    PEP 526, syntax for variable annotations.
    
    类型提示功能， py36的解释器并没有校验注释是否准确
    就像函数注释一样，Python解释器对变量注释没有附加任何特定的含义，只将它们存储在annotations类或模块的 属性中。
    Just as for function annotations, the Python interpreter does not attach any particular meaning to variable 
        annotations and only stores them in the annotations attribute of a class or module.
    In contrast to variable declarations in statically typed languages, the goal of annotation syntax is to provide an 
        easy way to specify structured type metadata for third party tools and libraries via the abstract syntax tree and the annotations attribute.

    与静态类型语言中的变量声明相反，注释语法的目的是提供一种通过抽象语法树和annotations属性为第三方工具和库指定结构化类型元数据的简单方法。
    
    只对函数参数做一个辅助的说明，并不对函数参数进行类型检查
    提供给第三方工具，做代码分析，发现隐藏的bug
    函数注解的信息，保存在 __annotation__属性中

    示例:
        introduced the standard for type annotations of function parameters, a.k.a. type hints. 
        This PEP adds syntax to Python for annotating the types of variables including class variables and instance variables:

        引入了功能参数类型注释的标准，也称为类型提示。这个PEP添加了Python的语法来注释变量的类型，包括类变量和实例变量：
        primes: List[int] = []
        captain: str  # Note: no initial value!
        
        class Starship:
            stats: Dict[str, int] = {}
        
        class Descring(object):
	        l:List[int]=[1,2,3]    # 类变量注释
	        d:Dict[str,int]={}     # 类变量注释
        
        函数注释：
        def add(x:int, y:int) -> int:
            return x + y
        
        print(add.__annotations__)
            'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
        
        # py36没有对注释做校验
        add(1,2)
        add("hello", "world")
        add(1.3, 2.4)
        以上都可以正常执行
    
    inspect模块
        提供获取对象信息的函数，可以检查函数和类，类型检查
        
        
### 异步发生器
    PEP 525, asynchronous generators.
    The asyncio module has received new features, significant usability and performance improvements, and a fair amount of bug fixes. 
    Starting with Python 3.6 the asyncio module is no longer provisional and its API is considered stable.
    asyncio模块已经获得了新功能，显着的可用性和性能改进，以及大量的错误修复。
    从Python 3.6开始，该asyncio模块不再是临时的，它的API被认为是稳定的。
    
    在py35中 异步生成器是不被支持的，但py36支持
    class Ticker:
    """Yield numbers from 0 to `to` every `delay` seconds."""

    def __init__(self, delay, to):
        self.delay = delay
        self.i = 0
        self.to = to

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        if i >= self.to:
            raise StopAsyncIteration
        self.i += 1
        if i:
            await asyncio.sleep(self.delay)
        return i

    # 以上等价与如下 异步生成器    
    async def ticker(delay, to):
        """yield numbers from 0 to *to* every *delay* seconds."""
        for i in range(to):
            yield i
            await asyncio.sleep(delay)
            
    * 异步上下文管理器
    class AsyncContextManager:
        async def __aenter__(self):
            await log('entering context')

        async def __aexit__(self, exc_type, exc, tb):
            await log('exiting context')
    
    * 异步文件读写
    class Reader:
        async def readline(self):
            ...

        def __aiter__(self):
            return self

        async def __anext__(self):
            val = await self.readline()
            if val == b'':
                raise StopAsyncIteration
            return val
        
### 异步理解
    PEP 530: asynchronous comprehensions.
    增加了在 列表，集合，字母推导式 和 生成器表达式中的使用  async for
    [i async for i in aiter() if i % 2]
    
    [await fun() for fun in funcs if await condition()]
    
### 一些经验上的区别总结

####  在Python 2中， ''字符串文字是一个字节序列。在Python 3中，''字符串文字是Unicode代码点的序列
       比如在py3
       >>> type('a')
	   <class 'str'>
        >>> type(b'a')
	    <class 'bytes'>
        >>> type(u'a')
    	<class 'str'>
        
     2，动态语言的局限
     Python还是一种动态语言，并且有大量的不变式在编译时没有被捕获，只能在运行时发现。不管您的测试覆盖范围有多好，这些不变式都无法通过测试全部检测到。
     这是动态语言的功能 / 局限性。多年来，我们的用户可能会在Python 3上发现很多其他错误
     
     3，Python 3 bytes仍然没有format()方法，因此替代方法实际上是字符串连接，这比%格式化的表现力倒退了一大步。
     4，Python 3的最初方法反映了许多开发人员和项目所做的愚蠢行为：尝试重写而不是执行渐进式演化。对于已建立的项目，大规模重写通常效果不佳。
     5，当我需要支持Python 2或什至更老版本的Python 3（例如3.5或3.6）时，非常难受，py37或py38更好？
        they want strings to be Unicode and don't want users to have to spend that much energy thinking about when to use str versus bytes.
## cpython改进
    1，基本类型
    字典的重新实现
        重新实现使用更紧凑的表示 基于由雷蒙德·赫廷格的建议 和类似PyPy字典实现。
        与Python 3.5相比，这使得字典的内存减少了20％到25％
    
    2，标准库
    新的文件路径标准库 pathlib
        已经实现了一种新的文件系统路径协议来支持类似路径的对象。
        所有在路径上运行的标准库函数都已更新，以配合新协议
    文件系统路径历来被表示为str 或bytes对象。这导致编写在文件系统路径上操作的代码的人们认为这样的对象只是这两种类型之一（int表示一个文件描述符不被视为不是文件路径）。
    这种假设阻止了文件系统路径的替代对象表示，例如pathlib使用预先存在的代码，包括Python的标准库
    Unfortunately that assumption prevents alternative object representations of file system paths like pathlib from 
    working with pre-existing code, including Python’s standard library.
    为了解决这种情况，os.PathLike已经定义了一个新的界面 。通过实现该 fspath()方法，一个对象表示它表示路径。然后，对象可以提供作为str或 bytes对象的文件系统路径的低级表示。
    这意味着一个对象被认为是 路径，如果它实现 os.PathLike或是一个str或bytes表示文件系统路径的对象。
    代码可以使用os.fspath()， os.fsdecode()或os.fsencode()显式地获得一个 str和/或bytes一个类似路径的对象的表示。
    
    内置open()函数已被更新为接受 os.PathLike对象，os以及os.path模块中的所有相关功能 以及标准库中的大多数其他功能和类。
    本os.DirEntry类和相关类pathlib也进行了更新来实现os.PathLike
    希望更新文件系统路径上运行的基本功能将导致第三方代码隐含地支持所有类似路径的对象，
    而无需任何代码更改，或至少非常小的os.fspath()代码（例如在操作开始时调用 代码）在路径样的对象上）
    with open(pathlib.Path("README")) as f:
	contents = f.read()

	
    >>> with open(pathlib.Path("README")) as f:
	    contents = f.read()
	    print(contents)
	    print(pathlib.Path("README"))

        README
        
    # py27的办法
    >>> import os.path
    >>> os.path.splitext(pathlib.Path("some_file.txt"))
        ('some_file', '.txt')
    >>> os.path.join("/a/b", pathlib.Path("c"))
        '/a/b/c'
    >>> import os
    >>> os.fspath(pathlib.Path("some_file.txt"))
        'some_file.txt'
    
    
    
    # pathlib常用操作
    from pathlib import Path

    filename = Path("source_data/text_files/raw_data.txt")
    
    1， 读文件，而不需要open()
    data_folder = Path("source_data/text_files/")

    file_to_open = data_folder / "raw_data.txt"
    print(file_to_open.read_text())
    
    也可以open了读取
    f = open(file_to_open)
    print(f.read())
    
    2，显示文件各种属性
    print(filename.name)
    # prints "raw_data.txt"

    print(filename.suffix)
    # prints "txt"

    print(filename.stem)
    # prints "raw_data"

    if not filename.exists():
        print("Oops, file doesn't exist!")
    else:
        print("Yay, the file exists!")

    3，常用方法
    方法列表
    （具体可看源码的细节）

    基本用法:

    Path.iterdir()　　#遍历目录的子目录或者文件

    Path.is_dir()　　#判断是否是目录

    Path.glob()　　#过滤目录(返回生成器)

    Path.resolve()　　#返回绝对路径

    拼接路径(目录中进行导航-官网说法)
    Path.exists()　　#判断路径是否存在

    Path.open()　　#打开文件(支持with)

    Path.unlink()　　#删除文件或目录(目录非空触发异常)

    基本属性:

    Path.parts　　#分割路径 类似os.path.split(), 不过返回元组

    Path.drive　　#返回驱动器名称

    Path.root　　#返回路径的根目录

    Path.anchor　　#自动判断返回drive或root

    Path.parents　　#返回所有上级目录的列表

    改变路径:

    Path.with_name()　　#更改路径名称, 更改最后一级路径名

    Path.with_suffix()　　#更改路径后缀

    #拼接路径

    Path.joinpath()　　#拼接路径

    Path.relative_to()　　#计算相对路径

    测试路径:

    Path.match()　　#测试路径是否符合pattern

    Path.is_dir()　　#是否是文件

    Path.is_absolute()　　#是否是绝对路径

    Path.is_reserved()　　#是否是预留路径

    Path.exists()　　#判断路径是否真实存在
    
    其他方法:

    Path.cwd()　　#返回当前目录的路径对象

    Path.home()　　#返回当前用户的home路径对象

    Path.stat()　　#返回路径信息, 同os.stat()

    Path.chmod()　　#更改路径权限, 类似os.chmod()

    Path.expanduser()　　#展开~返回完整路径对象

    Path.mkdir()　　#创建目录

    Path.rename()　　#重命名路径

    Path.rglob()　　#递归遍历所有子目录的文件
        
###  简化了类创建的定制(新协议) --- 可用于判定有多少子类继承自 该基类
        现在可以定制子类的创建而不依赖使用元类。新的init_subclass类方法将在每当创建一个新的子类时被创建
        # 为了允许零参数super()调用从init_subclass()实现中正常工作 ，自定义元类必须确保新的classcell命名空间条目被传播到 type.new（如创建类对象中所述）
        class PluginBase:
            subclasses = []
            def __init_subclass__(cls,**kwargs):
                super().__init_subclass__(**kwargs)
                cls.subclasses.append(cls)
        class Plugin1(PluginBase):
            pass
        class Plugin2(PluginBase):
            pass
        
        >>> PluginBase.subclasses
            [<class '__main__.Plugin1'>, <class '__main__.Plugin2'>]
        >>> p11 = Plugin1()
        >>> p11.subclasses
            [<class '__main__.Plugin1'>, <class '__main__.Plugin2'>]
       
    类属性定义顺序 现在被保留
    ** kwargs中的元素顺序现在对应于传递给函数的关键字参数的顺序
    添加了DTrace和SystemTap探测支持
    可以使用新的PYTHONMALLOC环境变量来调试解释器内存分配和访问错误
    
    
    typing typing模块接受了一些 改进
    
### datetime模块获得了当地时间消歧的支持
    在datetime中加入了 fold 属性，详情查看官方文档
    
###    该tracemalloc模块已经大大改造，现在用于提供更好的输出ResourceWarning以及为内存分配错误提供更好的诊断。
    有关详细信息，请参阅PYTHONMALLOC部分

### 加密模块 hashlib, ssl, secrets    
    hashlib模块支持BLAKE2，SHA-3和SHAKE哈希算法以及scrypt()密钥导出功能。
    hashlib ssl 模块支持 OpenSSL 1.1.0
    ssl模块的默认设置和功能集已得到改进
    
    密码模块 secrets
    The new secrets module has been added to simplify the generation of cryptographically strong pseudo-random numbers suitable for managing secrets such as account authentication, tokens, and similar
    添加了新的机密模块，以简化适用于管理机密（如帐户身份验证，令牌等）的强密码伪随机数的生成

### 描述符协议增强
    extends the descriptor protocol to include the new optional set_name() method. Whenever a new class is defined, 
    the new method will be called on all descriptors included in the definition, providing them with a reference to the class 
    being defined and the name given to the descriptor within the class namespace. In other words, 
    instances of descriptors can now know the attribute name of the descriptor in the owner class:
    （扩展描述符协议以包括新的可选 set_name()方法。每当定义一个新类时，将调用定义中包含的所有描述符的新方法，为它们提供对定义的类的引用，
    以及类名称空间中给描述符的名称。换句话说，描述符的实例现在可以知道所有者类中的描述符的属性名称：）
    
    class IntField:
        def __get__(self, instance, owner):
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise ValueError(f'expecting integer in {self.name}')
            instance.__dict__[self.name] = value

        # this is the new initializer:
        def __set_name__(self, owner, name):
            self.name = nam
    class Model:
	    int_field = IntField()
	
        
    
    