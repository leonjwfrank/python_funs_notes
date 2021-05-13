## 概念
    有穷观点: 有限数量的明确的指令
    能行: 每条指令都能机械的精确的执行
    
    计算模型: 以下几个模型是等价的
    哥德尔和克莱尼的 递归函数 模型
    丘奇 的 Lambda 演算模型
    波斯特的Post机 模型
    图灵的图灵机模型
    
    观点:
      计算机是数学家一次失败思考的产物
      总有数学命题，真假无法判定和证明
      
      能行和可计算 概念成为计算理论的基础， 其中图灵机成为现代计算机的理论模型

### 图灵模型
    现代计算机的模型，用机器来模拟人们用纸笔进行数学运算的过程，但比数值计算更简单
    1,在纸上写上或删除某个符号
    2,把注意力从纸但一个位置转向另一个位置
    3,在每个阶段，要绝对下一步但动作依赖于
        1, 此人当前关注的纸片某个位置的符号和
        2, 此人当前思维状态
    
    图灵机组成部分
    一条无限长的分格纸带，每格可以记录1格符号
    一个读写头，可在纸带上左右移动，能读出和擦写 格子字符
    一个状态寄存器，记录有限状态中的1个状态
    一系列有限控制规则
        某个状态，读入某个字符
        要改写成什么字符
        要如何移动读写头
        要改变成什么状态

### 抽象数据类型 ADT, abstract data type
    可以有多种实现方式
    计算机主要研究 问题，问题解决过程，以及问题解决方案
    包括计算复杂性理论和算法的研究


### 使用python实现数据结构

#### python基本操作的时间复杂度(大O数量级)
    当问题规模扩大后，程序需要的时间长度增长得有多快。也就是说，对于高速处理数据的计算机来说.
    处理某一个特定数据的效率不能衡量一个程序的好坏，而应该看当这个数据的规模变大到数百倍后.
    程序运行时间是否还是一样，或者也跟着慢了数百倍，或者变慢了数万倍.
    
    * 不是 所有的问题都可以找到复杂度为多项式级的算法。
    * 有些问题甚至根本不可能找到一个正确的算法来，这称之为“不可解问题”(Undecidable Decision Problem)。
    
#####    list
    平均情况假设参数是随机随机生成的。
    在内部，列表表示为数组。最大的成本来自超出当前分配大小的范围（因为所有内容都必须移动），或者来自在开始处附近插入或删除某处（因为之后的所有内容都必须移动）。如果需要在两端添加/删除，请考虑改用collections.deque
    
    操作(Operation)   平均(Average Case)    最坏情况(Amortized Worst Case)
    Copy                O(n)                    O(n)
    Append[1]           O(1)                    O(1)
    Pop last            O(1)                    O(1)
    Pop intermediate    O(k)                    O(k)
    Insert              O(n)                    O(n)
    Get Item            O(1)                    O(1)
    Set Item            O(1)                    O(1)
    Delete Item         O(n)                    O(n)    
    Iteration           O(n)                    O(n)
    Get Slice           O(k)                    O(k)
    Del Slice           O(n)                    O(n)
    Set Slice           O(k+n)                  O(k+n)
    Extend[1]           O(k)                    O(k)
    Sort                O(n log n)              O(n log n)
    Multiply            O(nk)                   O(nk)
    x in s              O(n)
    min(s), max(s)      O(n)
    Get Length          O(1)                    O(1)
    
    
#####    collections.deque
    双端队列（双端队列）在内部表示为双链表。 （为得到更高的效率，是一个数组而不是对象的列表。）两端都是可访问的，但是操作中间如查询，添加或从中间删除仍然很慢。
    中间操作建议使用list
    Operation       Average Case            Amortized Worst Case
    Copy             O(n)                       O(n)
    append           O(1)                       O(1)
    appendleft       O(1)                       O(1)
    pop              O(1)                       O(1)
    popleft          O(1)                       O(1)
    extend           O(k)                       O(k)
    extendleft       O(k)                       O(k)
    rotate           O(k)                       O(k)
    remove           O(n)                       O(n)        
    
#####    set
    设置差异s-t或s.difference（t）（set_difference（））和就地设置差异s.difference_update（t）（set_difference_update_internal（））的复杂度不同！
    第一个是O（len（s））（对于s中的每个元素，如果不在t中，则将其添加到新集合中）。第二个是O（len（t））（对于t中的每个元素，从s中删除它）。
    因此，必须注意哪个是首选集，具体取决于哪个是最长的集以及是否需要新的集。

    要执行类似s-t的设置操作，需要同时设置s和t。但是，即使t是可迭代的，也可以执行方法等效项，例如s.difference（l），其中l是一个列表
    Operation                           Average case                 Worst Case
    x in s                                  O(1)                        O(n)
    Union s|t                               O(len(s)+len(t))
    Intersection s&t                        O(min(len(s), len(t))       O(len(s) * len(t))      replace "min" with "max" if t is not a set
    Multiple intersection s1&s2&..&sn                                   (n-1)*O(l) where l is max(len(s1),..,len(sn))
    Difference s-t                          O(len(s))
    s.difference_update(t)                  O(len(t))
    Symmetric Difference s^t                O(len(s))                   O(len(s) * len(t))
    s.symmetric_difference_update(t)        O(len(t))                   O(len(t) * len(s))
    
    
#####    dict
    以下这些操作依赖于“最坏情况摊销”的“摊销”部分。根据容器的历史记录，各个操作可能会花费惊人的时间。

    对于这些操作，最坏的情况n是容器曾经达到的最大大小，而不仅仅是当前大小。例如，如果将N个对象添加到词典中，然后删除N-1个，则该词典仍将为N个对象调整大小（至少为N），直到再次插入为止。
    为dict对象列出的平均情况时间假设对象的哈希函数足够强大，以至于不常见冲突。平均情况假设参数中使用的键是从所有键集中随机选择的。

    注意:有一种快速的命令可以（实际上）只处理str键。这不会影响算法的复杂性，但是会显着影响以下恒定因素：典型程序的完成速度。
    Operation           Average Case            Amortized Worst Case
    Copy[2]                 O(n)                       O(n)
    Get Item                O(1)                       O(n)
    Set Item[1]             O(1)                       O(n)
    Delete Item             O(1)                       O(n)
    Iteration[2]            O(n)                       O(n)
    
## 栈的应用
    1, 成对符号的匹配算法
        如 ([{}])
    2, 十进制与二进制的转化
    3, 表达式转换
    4, 后缀表达式求值
    * 括号匹配过程中，栈结构在匹配的时候如果有相匹配的成对符合，不压入直接返回。
    
## 队列 Queue 双端队列 Deque
    有次序的数据集合
    压入的一端叫 尾端
    取出的一端叫 首端
    实际应用: 打印机，键盘
    操作定义
    Queue(), 创建一个空队列，返回Queue对象;
    enqueue(item):将数据项item添加到队尾。无返回值
    dequeue():  从对首移除数据项，返回值为对首数据项，队列被修改。
    isEmpty(): 测试是否空队列，返回布尔值
    size():  返回队列大小
    
    
## 链表 节点Node
    单链表
    每个节点至少包含两个信息，数据元素本身和下一个数据的位置
    
    
    双端链表
    前后元素的地址都有
    
## 递归 recursion
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
    
    实践:
    3, 分形树
        海龟作图 turtle
        曼德博图像，自相识图形
    
    4, 谢尔宾斯基三角形
    
    5, 汗诺塔
    
    6, 探索迷宫
        
   
## 递归分治策略
    分治
        大问题化整为零，分别解决
    应用    
    表达式求值
    优化问题
        找到问题的最优解
        
    找零兑换问题
        自动找零机，最少硬币
        方案1，贪心策略 Greedy Method  解法
        分治策略解决问题时，每次解决问题最大的一部分
        依赖货币体系
        方案2，递归解法
        肯定可以找到最少硬币组合最优解
     
        方案3，动态规划
        从最简单情况开始到达所需找零的循环
        其每一步都依靠以前都最优解 来得到本步骤都最优解，直到得到答案
        
    
        * 思路，
            从小 到 大求解币值的最优组合解
            两个列表，
            一个用于存储已计算得到的最优组合解
            一个用于存储当前额度 的解的组合 的最后使用的币值面额，在动态规划里，一般是最大的
        
    * 动态规划问题 博物馆大盗-利益最大化
    大盗面临的价值选择
    item    weight      value
    1        2            3
    2        3            4
    3        4            8 
    4        5            8
    5        9           10
    
    m(i,W)记为  前i(1<=i<=5)个宝物中，组合不超过W(1<=W<=20) 重量，得到的最大价值
    m(i,W)应该是m(i-1,W) 和m(i-1,W-Wi)+vi 两者最大值
    我们从m(1,1)开始计算到m(5,20)
    m(i,W)={0: "if i=0",
            0: "if W=0",
            m(i-1,W):  "if wi>W",
            max{m(i-1, W), vi+m(i-1,W-wi)}: otherwise}
    
    做表来计算最佳选择
    i/W     0   1   2   3   4   5   ...
    0       0   0   0   0   0   0
    1       0   0   3   3   3   3
    2       0   0   3   4   4   7
    3       0   0   3   4   8   8
    4       0   0   3   4   8   8   
    5       0   0   3   4   8   8
    m(5,5)=m(4,5)=max(m(3,5),m(3,0)+8)
    
    #博物馆大盗 代码 structure/base_code/syncThiedmuseum 
    
    
    