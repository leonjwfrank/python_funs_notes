### 附 递归，迭代，循环，遍历
    
####    循环（loop）
    指的是在满足条件的情况下，重复执行同一段代码。比如，while语句。
        while n < 10:
            print(n+1)
    迭代（iterate），指的是按照某种顺序逐个访问列表中的每一项。比如，for语句。
    自动迭代的一种更优雅的方法是使用for循环。使用此方法，我们可以迭代可以返回迭代器的任何对象，例如列表，字符串，文件等
        1,关键字 yield
            def iter_yie(n):
                while n:
                    n -= 1
                    yield n
            ite_100 = iter_yie(100)
            >>> next(ite_100)
                99
                
        2, 循环设计
        ite = iter(range(10)
        next(ite)
        for i in ite:
            print(i+1)
        自定义迭代类型
        class PowIter:
        """Class to implement an iterator of powers of iter"""

            def __init__(self, max = 0):
                self.max = max

            def __iter__(self):
                self.n = 0
                return self

            def __next__(self):
                if self.n <= self.max:
                    result = 2 ** self.n
                    self.n += 1
                    return result
                else:
                    raise StopIteration
        a = PowIter(4)
        >>> i = iter(a)
        >>> next(i)
            1
####    遍历（traversal）
    可迭代对象都可以被遍历
    指的是按照一定的规则访问树形结构中的每个节点，而且每个节点都只访问一次。
    1, 简单列表遍历
    for i in list(range(100)):
        print(i)
    
    ```python
        class Node:
        def __init__(self,data):
            self.left = None
            self.right = None
            self.data = data

        def inOrder(root):
            if root:
                inOrder(root.left)
                print (root.data)
                inOrder(root.right)

        def preOrder(root):
            if root:
                print (root.data)
                preOrder(root.left)
                preOrder(root.right)

        def postOrder(root):
            if root:
                postOrder(root.left)
                postOrder(root.right)
                print (root.data)

    #making the tree 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print inOrder(root)
    #4 2 5 1 3
    print preOrder(root)
    #1 2 4 5 3
    print postOrder(root)
    #4 5 2 3 1
        
####    递归（recursion）
    1，概述
    问题分解为更小的问题
    持续分解，直到可以用非常简单的方法解决
    函数:调用自身
    def listsum(lis):
        # 递归调用
        if len(lis) == 1:
            return lis[0]
        else:
            return lis[0] + listsum(lis[1:])
    
    递归三要素:
        1,递归算法必须有一个基本结束条件(最小规划问题的 直接解决)
        2,递归算法必须能改变状态向基本结束条件演进(减小问题规模)
        3,调用自身。
    
    # 应用 用递归实现十进制转为 任意进制
    ～code 见notebook
    
    2，递归实现
    
    当调用一个函数被调用时，系统会把调用时的现场数据 压入到系统调用栈，每次调用压入栈的现场数据称为  栈帧
    当函数返回时，要从调用栈的栈顶取得返回地址，恢复现场，弹出栈帧，按地址返回
    2.1,深度限制  # 电影 前目的地predestin，恐怖邮轮Triangle
        避免无限递归 或 避免超出系统调用栈的限制
        python递归 sys.getrecursionlimit() 获得递归深度  setrecursionlimit(3000)
    指的是一个函数不断调用自身的行为。比如，以编程方式输出著名的斐波纳契数列
    #  递归， 默认最多1000层
    @functools.lru_cache(maxsize=None)   # 计算性能
    def fb(n):  # 第几个fbnc数
	    if n <= 2:
		    return 1
	    else:
		    return fb(n-1) + fb(n-2)
    实例见code        

#### 迭代器和生成器
    1, 生成器yield
        一类特殊的迭代器，py中自动实现类 iter 和 next
    2，迭代器概念和协议
    在py中，迭代器遵循迭代器协议：必须拥有__iter__方法和__next__方法
    实现了 __iter__()  和 __next__()的类
    
    举例:
    print('__next__' in dir(range(12)))  #查看'__next__'是不是在range()方法执行之后内部是否有__next__
    print('__iter__' in dir(range(12)))  #查看'__iter__'是不是在range()方法执行之后内部是否有__next__

    from collections import Iterator
    print(isinstance(range(100000000),Iterator))  #验证range执行之后得到的结果不是一个迭代器
    
    
    3，迭代器模式类的实现
    import itertools
    # 迭代器遵循迭代器协议：必须拥有__iter__方法和__next__方法。
    class Prime(object):
    """ An iterator for prime numbers 
    无限迭代器，生成指定两个数之间的质数序列"""

    def __init__(self, initial, final=0):
        """ Initializer - accepts a number """
        # This may or may not be prime
        self.current = initial
        self.final = final
        
    def __iter__(self):
        return self

    def __next__(self):
        """ Return next item in iterator """
        return self._compute()

    def _compute(self):
        """ Compute the next prime number """

        num = self.current
        
        while True:
            is_prime = True
            
            # Check this number
            for x in range(2, int(pow(self.current, 0.5)+1)):
                if self.current%x==0:
                    is_prime = False
                    break


            num = self.current
            self.current += 1

            if is_prime:
                return num
            
            # If there is an end range, look for it
            if self.final>0 and self.current>self.final:
                raise StopIteration
    