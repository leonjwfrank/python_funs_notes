
###########++++++++++++++++++++++++++++++
## Law of demeter (LoD:隐藏信息原则/最小特权原则)
    每个单元对其他单元的了解都有限：只了解与当前单元“紧密”相关的单元。
    每个单元只能与朋友交谈；不要跟陌生人说话。
    只与您的直系朋友交谈
    此原则规定软体模块 仅拥有其合法目的所需的信息和资源.
    如: 对象应该避免调用另一个方法返回的对象的方法, 简单表述为 仅使用一个点. 那么a.m().n() 就违反了demeter原则.
    就像是 一个人想要一只狗散步,不会指挥狗的腿直接走路,取而代之是命令狗,然后让狗调用自己的腿.

    优点:
        遵循demeter定律的软件最后 倾向于 可维护 和 适应性强,由于对象依赖其他对象的内部结构较少,因此可以更改对象容器而无需重新构造调用者.
        较低的类响应RFC, 响应于调用该类的方法而可能调用的方法数量,可以降低软件错误的可能性.
        同理的, 类的方法数量的增加,导致软件错误的可能性增加.
        又如多层架构可以被认为是软件系统中实现 demeter系统的机制,分层体系中,每一层代码只能调用该层代码,不能调用下一层.
    缺点:
        尽管LoD增强了软件系统的适应性,但它能导致必须编写许多包装方法才能调用传播到组件.
        这可能会增加时间和空间开销.
        LoD导致接口狭窄. 因为每种方法都需要知道与之紧密相关的对象的一小部分方法,因此只能访问完成其工作所需的信息.

    give the clerk your wallet and let him/her retrieve the $25  # 给店员整钱.然后让他们找零
    purchase method   # 购买方式, 只给合适的钱最效率

## 依赖注入  google tech
    disseminate a wide spectrum of views on topics including current affairs science medicine, engineering business humanities, law entertainment arts
    就时事科学医学，工程商业人文，法律娱乐艺术等话题发表广泛的看法
    disclaimer  # 免责声明
    the views or opinions expressed by the guest speakers are solely their own and do not necessarily represent the views or opinions of platform  # 
 演讲嘉宾表达的观点或观点仅是他们自己的观点，不一定代表平台的观点或观点
###  clean code 干净的代码
    ask for things   # 索要东西
    don't look for things  # 不要寻找东西
    显式的胜于隐式的  Stating the obvious
    cost of constructor always for things     #     构造函数的总成本

    law of Demeter      #     得墨meter耳定律
    where have all the new operators gone   # 所有新运营商都去了哪里
    presented by the testability corps   #     可测试性团队提出
    
    ## 为什么代码很难顺序测试
        测试某个方法,需要首先实例化它
        test a method you first need to instantiate an object   # 测试你需要首先实例化对象的方法
        constructor which make the instantiation process really hard # 但是所在构造者,实例化非常困难.
        not only do they put things in the constructor  # 不仅需要将事务(参数或对象)放入构造者
        people put code into static initialization classes # 人们通常将代码放入静态构造类中
            which makes the code again even harder to instantiate because static init class probably goes out and reaches to some kind of singleton class # 静态构造类使得代码更加困难,因为静态构造通常 不匹配或者触发一些如单例类
        in order to test any kind of instance methods to instantiate the class  # 为了测试任意实例的方法而去实例 这些类

        specifically the system under test  # 特别是被测系统
        collaborators test-double collaborators(fakes,dummies,mocks,stubs,spys,etc.)  #合作者/测试双重合作者
    如果有一个客户端比如文件document, client类,如何测试这个client类?
    ## suggestions from audience    # 听者的建议 
    you would actually have to instantiate a web server that comes up  # 一般情况需要为测试建立一个测试服务器
    you would have to set up the test server with document, and instance the document then pass the URL that's donna have localhost to some port .... # 你需要准备文档,并实例化文档,然后发送到测试服务器上的端口
    this how cumbersome the whole process    # 这整个过程是笨拙的

    injector 依赖注入方式使得该实例化过程更容易
    why the previous slide we could have could not have simply instantiated sth # 上一页幻灯片我们没能执行测试,这一次我们可以简单实例化
    this particular thing is a lot more testable because i can aways pass in a mock HTML  # 特殊事务由许多可测试性,可以总是通过一个模拟的返回来执行HTML的client测试

    even through we rid of server,new problem is every time we need to instantiate in a mock http client we have to prime it with an expectation, and have a prime to return the value whcih we want
        # 虽然我们摆脱了服务器限制,但新的问题是每次我们需要实例化一个http客户端时都需要准备预期的文档,并准备一个我们需要的返回值
    the simple way is prime the HTML code that i want and shove it into my field variable what i need.  # 简单的方式就是直接准备我们需要的HTML代码并放入到我们 需要的构造函数的地方. 

    we only needing sth from there in order to traverse sth  # 我们只需要从那里获取,遍历他们并获得我们真正需要的

    because we have a lot of depond on a document suppose you have a printer # 为了支持打印机我们有许多依赖在这个文件上
    if you want to instantiate a printer and test out a print list that you presumably have to pass a document # 如果你想初始化一个打印机并且测试 打印列表,想必(presumably)你不得不传入一个文件

    it will be nice if initantiate printer we shove into the doc constructor which i wat to print
    如果在初始化printer打印机时,我们想要打印的文档对象就已经传入构造器,那就太好了
    I do not want to go and mock out all the pieces over and over again. # 我们并不想一次又一次的去制作所有的文件

    mixing the object graph construction with object lookup instead of asking what we     #  混合对象图构造而不是 问我们需要什么去构造它

    I will demonstrate this through this particular class                # 我将演示这个原理, 通过这个特别的类
    imagine that just like a doc you had a class called the car          # 想象那样 你有一个名为 car的类
    have another class named engine factory, and car wanted to get a hold of the engine in the previous class what we did is we instantiated the engine the diet of the http client                       # 另有一个engine 的类,car类要在先前的类持有这个engine, 我们需要做的时实例化这个engine类并 投入http 客户端
    in this case is the engine factory          # 在此例中为engine工厂

    now isn't this a little bizarre that a car knows how to build a factory and then asks the factory to build an engine which then it saves inside of itself    # 现在有些奇怪的是 car 类知道如何新建一个工厂,然后询问这个工厂去构建一个发动机engine类, 它将保存在它自己中.

    deal with concrete objects do we realize just how silly it is for a constructor to be asking for the factory  # 如此处理具体对象, 我们发现是如此愚蠢只是为了建造者询问工厂

    produces sth that are asking for the item directly   # 制作某种东西,那样可以访问这些元素 更直接

    instantiating small portions of your application    # 实例化你程序的每一个小的部分
    same drill every single time you instantiate a small portions  # 同样的转孔在每一次小的部分单独的实例化  

    poke out the objects a little bit and assert some ouput,  # 摘出程序的一小部分,然后断言一个判断

    you instantiate some other piece of portion of the application   # ,你可以实例化一些程序的其他部分

    poke at it and assert some output            # 摘出它并断言一些输出

    instance doc directly or indirectly so it's a kind of a transtive problem # 直接或非直接的实例化doc, 它是一种传递问题

    bad:
        collaborators needed to test printer   # 合作者需要测试打印机
        complexity     # 复杂度
        opacity    # 不透明度

### Cost of Construction
    1,Test has to successfully navigate the constructor each time instance is needed  # 测试很难在要实例时都 成功导航到构造函数
    2,Objects require construction  # 对象构造,
        Hard to construct objects are a real pain to test  # 测试时构造对象是真正的痛点.
    3, would like to have nothing but assignments inside if the constructor you simply  # 如果只是构造函数,除了分配什么也不想做
    4, save it into your local variable in your local field  # 保存它到你本地值域

### service locator 
    service locator what it tried to do Problems it attempts to solve   # 本地服务尝试解决如下问题
    - Resolution of dependencies without calling new in your production code  #解决依赖关系而无需在生产代码中调用new
    - Inversion of Control   # 控制翻转 
    - Allow for looser coupling    # 松耦合
    - Interchange wiring for testing   # 用于测试的交换接口

    Shortcomings:
        - Service Locator encourages ambiguous API's   # Api服务定位模棱两可
        - Difficulties wiring the locator up for tests  # 定位器连接困难
        - Often uses global mutable state           # 经常造成全局易变的状态 
        - Violates the spirit of the Law of Demeter   # 违反最小有效特权原则(迪特米勒)

    we need search through service locator to get the object of interest # 在service locator 我们需要 深入搜索以获得感兴趣的对象

    用途
    Context       # 语境上下文
    Better then a singleton       # 好于单例
        if you had static look up of services this is an improvement. It is testable but it is not pretty.  #
如果您对服务进行静态查找，这将是一项改进。这是可测试的，但不是很漂亮。
        much better paradigm than having a global state where you store your singleton    # service local是比存储静态单例更好的范例

    Hides true dependencies     # 隐藏真正的依赖    
    Mixing Responsibilities   # 混合责任
        Lookup
        Factory
    Need to have an interface for testing    # 需要有一个测试界面
    Anything which depends on Service Locator now depends on everything else    # 一切取决于服务定位器依赖于其他什么事务

    # Explan 解读如下
    all of a sudden had a new dependency, you need deal with it in step  # 当处理的对象突然有了新的依赖, 你需要按步骤处理它
    you would simply declare the new constructor and you would immediately know which tests do not compile #您只需声明新的构造函数，便会立即知道哪些测试无法编译
    
    because now there's a new parameter in the constructor    # 因为现在这里有新的参数在构造器中
    you can go into those tests and then fix them whereas     # 您可以深入这些测试并且修复他们
    but the tests in all over the place are starting to fail and you are not quite sure why # 但是测试在各个地方仍然失败,并且您不知道为什么

    the service locator knows that other services and objects and cetera whether the house needs them  # 服务定位器知道其他服务和物件以及房屋是否需要它们

    Now, you in order to to give somebody a house you have to give a service locator, 
    in order to give a service locator you have to basically your home application not very reusable  # 您为了给别人提供一个房子,你需要一个服务定位器,为了得到一个服务定位器,你需要基础构建你的主体程序,那样不是完美可重用的

    in the constructor we specify things that we actually mean  we needed # 在构造函数中，我们指定实际上我们真正需要的东西
    I immediately know what else needs to be instantiated  #如此我可以立刻清晰的知道哪些需要实例化

    示例:
    class HouseTest(object):
        def testServiceLocator():
            Door = Door()
            Roof = Roof()
            Window = Window()
            House = House(Door, Roof, Windows)

    we are mixing the responsibility of object look up and object   # 
    bunch of setter methods where we can externally set the dependencies  # 绑定方法我们可以外部设置依赖
    everything depends on a service locator now depends on everything else whether you like it  # 所有依赖于服务定位器的事务都依赖于其他事务.无论你是否喜欢

## Similar Partners-in-Crime   # 类似于 合伙的 其他定义名称
    Other names this anti-pattern can be disguised as     # 其他类似于 自反模式的定义
    Registry                # 登记处
    Locator                 #     定位器
    Context                 #    语境
    Manager                 #   经理
    Handler                 #     处理程序
    Environment             #     环境
    Principle           #     原理


### Myth about DI (Denpendon Injector)   # 依赖注入神话
    依赖注入是一种对象接收其依赖的其他对象的技术。这些其他对象称为依赖项。在典型的“使用”关系中，接收对象称为客户端，而传递的（即“注入”）对象称为service。将服务传递给客户端的代码可以有很多种，称为注入器。注入程序会告诉客户端要使用的服务，而不是由客户端指定它将使用的服务

    1, DI makes refactoring hard        # 依赖注入使得重构更加困难
        If a child object needs a new parameter then i have to pass it through all of its parents  #如果子对象需要一个新参数，那么我必须将其传递给它的所有父对象

    2, Because of LoD(最小权限原则) you should never ask for enything you donot directly need  # 不应该询问不是直接需要的对象

    3, Parent object does not make a child it asks for child So if child needs a new dependency the parent is not aware
    # 父对象不会让孩子创建子对象，所以如果子对象需要新的依赖关系，父对象将不知道


    reconcile this three

    doork             # 门
    doorknob          # 门把手

    i have one factory serves a whole bunch of objects   # 我有一家工厂为一大堆物品服务
    typically you actually have in theory you actually only need one factory # # 通常您在理论上只需要一个工厂
    for all of the objects of the same lifetime in practice  # 为所有对象在相同生命周期实践
    we would really have ridiculously large factory   # 我们将有一个可笑的大的工厂

    you really only need one factory plus couple of break down to the classes are not ridiculously large per object lifetime # 你真的只需要一个工厂，再加上几个细分，这并不是很荒谬的
    in typical application you have your long-lived objects you have your session   # 在特别的程序中有 长生存周期会话对象

    you have your request scope objects plus you have some objecets that are really short-lived typically   # 你有你的附加请求范围对象 却只有极短的生存周期

    those are rare you typically just stick to your request scope so in theory you can get away with four factories  # 那些很少见，您通常只坚持您的要求范围，因此理论上您可以放弃四家工厂


### Object Lifetime
    Constructor injection:   # 建设者 注入器
        Only inject objects whose lifetime is equal to or greater then 'injectee'  # 仅注入寿命等于或大于“被注入者”的对象

    Pass in As Method Parameters at the time of execution:   # 在执行时作为方法参数传递
        Objects whose lifetime is shorter than the injectee    # 对象整个生命周期比 注入对象短.


    比如为一个house对象注入door对象, 此door对象需要生命周期大于等于 house对象
    you typically pass that through a stack   # 您通过一个特别的方式传递一个堆栈
    you group your equally little objects together  # 您将同样小的物体组合在一起
    you instance all equally lifetime objects together  # 所有相同生命周期的对象组合在在一起
    basically phases   # 以上为基本阶段



### Null checking   # 空类型检查
    common practice          # 惯常做法
    paranoid programming             # 偏执编程狂
    people love to put null checks everywhere   # 人们喜欢在任何地方检查空类型

    示例:
        class House(object):
            House(Door):
                PreConditions.checkNotNull(door);
            def getColor():
                return red
        def testHousePainting():
            house = House(null)
            Color = house.getColor()
            assertEqural(RED)

    a precondition check that says    # 前提条件检查提示
    actually that from a testing point of view it makes my test much hard # 以上代码让测试执行更困难


### Alawys ask for things
    Abandon the new operator(in 99% domain classes)   # 放弃新的操作者
        All of the new operators end up with application configuration objects(which either works or doesnot integration tested) # 
所有新的运算符最终都带有应用程序配置对象（可以运行或未经过集成测试）
    

    Since you do not construct collaborators, there is no need to know about objects you do not directly use 
        Construction is done by a DI Container or Factories and Builders  # 由于您不构造协作者，因此无需了解您不直接使用的对象建造工作由DI容器或工厂和建筑商完成


    Pile of Objects
        Business logic            # this is the stuff that does work in your application  真正有用的东西,也是bug的产出地
        This is why you are writing code  #
        Responsibility is business logic, domain abstractions # 对象责任是业务逻辑，域抽象

        Small tests are very easy to write & understand 
            Happen naturally when using DI   # 使用DI时自然发生
        When everything works in Integration tests   Great  # 在集成测试中执行所有工作,太棒了
   
        When the wiring is wrong   # 当注入接口对接错误
            Failure it often blows up   # 失败经常发生
            Scenario tests are needed to ensure that   # 场景测试需要确定依赖性
            objects are wired together properly  # 对象 需要预先对接在一起
        When the system fails in some small way  # 当系统在某些小的方面失败
            Bug with specific class missing unit test  # 缺陷在没有单元测试的特殊的类中发生

    Pile of New Keywords
        Provider Objects      # 提供对象
        Factories             # 工厂们
        Builders              # 建造者们
        This is how you get the code you write to work together   # 是如何从同事那里获取代码的方式

        Responsibility is to build object graphs     # 关键责任是建立对象图

    make sure that the instantiation of the database works correctly but i do not want you to actually go off   #确保数据库的实例正常工作，但我不希望您实际离开
    and call any kind of sequel methods on it   # 以及在其上调用任何后续的方法

    by having the separation you can actually test both the factories # 分离后，您实际上可以测试两个工厂

    the business logic in isolation if you mix them together  #如果将它们混合在一起，则会孤立地处理业务逻辑

    it is very easy to basically call a method that starts doing the real work instantiate # 基本上调用一个开始实例化实际工作的方法非常容易
    do more work and so on and so forth     # 现在及未来做更多工作

    it turns out that our factories if you file the dependency injection the way  # 事实证明，如果您提交依赖项注入，我们的工厂

    it is recommend that it turns out that it is really easy to instantiate things you simply look   #建议并且事实证明 实例化您看起来很简单的东西真的很容易
    you simply look at the constructor  # 你只需简单看一下构造函数
    in order to instantiate a house i need to instatiate these other things  # 为了构造房子我需要构造其他事务
    as a matter of fact the whole process is so automatic  # 事实上，整个过程是如此自动化
    you can build a framework that simply uses reflection to look at the constructor  # 您可以构建一个仅使用反射来查看构造函数的框架
    

    you get a full closure one such framework is juice   # 你得到一个完全封闭的框架就是果汁

    dummy: does not implement any real method # 通常没有所有方法的操作
    dummy would be like your now value object correct is that what 

        essentially a null value object  # 本质上是空值对象

        例子:
            a house might have whole bunch of methods   # 一所房子可能有很多方法
            locked, paint
            call a lock method presumably  # 我要调用 锁的方法
            house has to collaborate with the doors and the windows in order to get the whole house locked down  # 房子必须与门窗配合才能锁住房子
            if i  test for the lock method i would pass in a real door and real windows  # 如果我测试锁定方法，我会通过一扇真实的门和真实的窗户
            because i wanted to assert that the whole locking precess works  # 因为我想断言整个锁定状态时正常的

            if i am painting the house that method has nothing to do with doors or windwos

            so i should not be forced to instantiate doors and windows inside # 粉刷与门窗无关,我不应该被迫实例化内部的门窗

            for getting the whole problem of dummies even if i have dummy door hanging around i still donot really want to instantiate and pass it  # 即使我有假门悬而未决也要解决整个虚拟人的问题，我仍然真的不想实例化, 直接通过它

            because they kind of suggested the reader of the test that somehow the door is involved in a whole painting  # 因为他们建议测试的读者以某种方式将门包含在整个粉刷中

## quiz
        like what are the scenario you think will be a good case for dummy obj

        you would use a dummy object if you know that in your execution path # 如果您知道执行过程中会使用一个虚拟对象
        you actually going to be dispatching parameter      # 你实际上将要调度参数
        which means a knoll would cause a nullpointerexception  # 这意味着小节将导致nullpointerexception
        you really do not care about this particular object because it is something like a logger or locks  # 您实际上并不关心此特定对象，因为它类似于记录器或锁
        you just want a no operation to happen over there that is what dummy for   # 您只想在那儿进行任何操作，这就是 虚对象

        dummy is needed when i dispatch but not now use it   # 虚对象是需要当我调度 但不使用.

        a dummy because it says not only is it not needed nobody's ever dispatching # 因为它不仅不需要,而且没有人调度

## pythonic injector

    1, 简洁性
    2, 没有全局状态,
        可以拥有任意数量的Injector实例,每个实例具有不同配置,
        每个实例在不同范围有不同对象
    3, 与静态类型检查基础结构协作,API提供了尽可能多的静态类型安全性,并且只有在没有其他选择的情况夏才破坏它.
        如 injector.get方法,以便静态声明injector.get(sometype)以返回 somtye实例
        因此使mypy等工具可以使用该类型正确检查代码
    4, 客户机代码只知道依赖注入到它所需要的延申
    5, 库解析
    常用模块
    injector
        Module              # 配置注入器和提供者
            使用: class db_module(Module):
                    @provider
                    def provide_db(self, conf:def_conf):
                        conn = sqllite3.connect()
                        cursor = conn.cursor()
                        cursor.execute(sql_create)
                        return conn

        provider            # 装饰模块方法的装饰器，注册一种类型的提供者
            使用:
            @provider
     
        inject              # 装饰器声明要注入的参数
            使用:
            class RequestHandler(object):
                @inject
                def __init__(self, db:sqlite3.Connection):
                    self._db = db
                def get(self):
                    cursor = self._db.cursor()
                    db_res = cursor.execute(sql_query)
                    return db_res.fetcall()
        injector
            :param modules: Optional - a configuration module or iterable of configuration modules.
                Each module will be installed in current :class:`Binder` using :meth:`Binder.install`.
                Consult :meth:`Binder.install` documentation for the details.
            :param auto_bind: Whether to automatically bind missing types.
            :param parent: Parent injector.
        singleton
            A :class:`Scope` that returns a per-Injector instance for a key.

            :data:`singleton` can be used as a convenience class decorator.

            >>> class A: pass
            >>> injector = Injector()
            >>> provider = ClassProvider(A)
            >>> singleton = SingletonScope(injector)
            >>> a = singleton.get(A, provider)
            >>> b = singleton.get(A, provider)
            >>> a is b
            True





