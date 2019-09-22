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
    