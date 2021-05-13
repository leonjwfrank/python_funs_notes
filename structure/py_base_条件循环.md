## 1. 循环&条件
    h3. 条件
        if, if...elif...else
        条件三元表达式:
            Z if X else Y
            smaller = x if x>y else y
    h3. 循环 (避免重复操作放到参数中)
        while 条件循环
        for 迭代循环
            原理 :遍历序列成员, 依次访问可迭代对象(序列, 迭代器)
            使用场景:
                序列
                    字符串,列表,元组
                        序列项, 序列索引, 项,索引(enumerate())
                    字典 for key, value in dict.items()
                迭代器
                    自动调用,直到捕获StopItoration异常结束循环
                    迭代器对象next()方法,调用后清除本项目,进入下一个项目
        ** else 子句只在正常完成后执行,break会跳过else子句
        while...else... 
        for...else...
    h3. 循环控制
        break  停止整个循环
        continue    (类似控制:while...for)
            验证成功后,跳过本次,进入下一次
            如:if 条件成真, for 有下一个迭代对象
        pass
            空语句, 可用在 if/elif/else, while/for, def/class, try/except/finally
    h3. 控制流BIF
        range(start,end,step=), 完整语法
        简略语法 range(end),range(start, end)
        xrange()---(性能更高)不会在内存中建立
        enumerate() 每次循环返回tuple(索引,元素对)
        reversed() 反序访问
        zip()
            聚合列表
                从多个等长序列,依次各取出一个元素,组成元组
            分解聚合
                zipped=zip(a,b)
                a,b = zip(*zipped)
                如:a = [1,2,3,4,5]
                b = [6,7,8,9,0]
                zipped1 = zip(a[0:2],b[0:2])
                na,nb = zip(zipped1)
                na ((1, 6),)
                nb ((2, 7),)
        sorted()  (iterable, emp=, key=, ) 
        
    h3. 生成器. genarate
        含义: 本质为函数, 允许返回一值,然后暂停代码执行, 随后恢复代码执行
        对比列表解析:需要一次生成所有数据
        生成器表达式
            结合了 列表解析&迭代器
            在循环中一边循环一边计算后续元素,优化了内存
            yield语句
                立即返回一个值
                下一次迭代生成器函数时，从yield语句后的语句继续执行，直到再次yield返回，将终止
                
        生成器编写方法
            生成器表达式
                打印元素
                    for
                    next() 直到计算到最后一个元素
                    如:寻找文件最长行
                        max(len(x.strip()) for x in open(''.txt))
                        优化后:
                            sum(len(word) for line in[for word in line.split()])
                函数实现
                    yleld 关键字
                    类似函数,return 改为yleld, 遇到yleld就返回,可用有多个yleld
                    def gep():
                        yleld__
                    打印元素
                        items = gen()
                        for 循环 for i in items print()
                        next()  items.next()
    h3. 生成器实现的 协程(协同程序)
        可以用yield实现
        可以独立运行的独立函数调用，函数可以暂停或挂起，并在需要的时候从离开的地方继续或重新开始。
        相互前进。
        
        def  even_num(max):
            n=0
            while n<max:
                yield n
                n += 2
        for i in even_num(10):
            print(i)
            
    h3. 迭代器
        目的
            为 类序列对象提供类序列接口, 如字典的键 文件的行
            用于迭代不是序列却 需要表现出序列行为的对象
        本质
            next()方法的对象并非索引计数
        创建
            iter(obj) str, list, tuple
        访问
            next(iter, obj)            
        列表
            list()
        使用
            序列
                for 循环 for i in seq 
                while 1:
                    try:
                        i = next(fetch)
                    except StopIteration:
                        break
                    finally:
                        do_something
            字典:
                dict.keys(), ditc.values(), dict.items()
            文件:
                自动调用 readline()
                for eachline in open(*.txt)                
        拓展
            适用 any()/all()
            判断迭代:
                from collections import iterable
                isinstance('abc', iterable)                                

        警告
            迭代时无法修改
            迭代时列表的改动会立即反应到迭代条目上
            字典不能改变
            限制
                不能复制,只能创建另一个迭代器
                移动方向,不能重新开始

    h3. 列表解析
        基本语法:
            expr for item in iterable
        拓展版本:
            expr for iter in iterable if cond_expr
        多层循环
            expr[a, b]for x in iter ofr b in iter2
            如: 计算文本文件 f=open(''.txt)
            单词总数
                len(wotd ofr line in f for word in line.splot())
            字符总数
                sum(len(word) for line in f for word in line.split())
        同时使用dict的键,值
            expr(x,t) for x,t in dict.items()
        与zip结合使用
            x**2 for (x,y) in zip(seq1, seq2) if y > 10
        三次函数调用
            map(lambda x:x**2, range(6))
        一次函数调用
            [x ** 2 for x in range(6)]