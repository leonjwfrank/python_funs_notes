
h2. 序列
        含义:
            成员 有序排列, 通过下标偏移量访问
        包括  str, list, tuple
    操作符:
        标准类型操作符
        序列类型操作符
            成员关系
                True/False, in, obj in seq
                not in 
            连接 
               推荐	 seq1.extent(seq2)
               + seq1 + seq2
            重复
               * seq*expr
            切片
               seq[ind]
               seq[ind1:ind2]
               [], [:], [::]
            基本样式:
               [下限:上限:步长]
               上限本身, 不包括在内
            拓展样式
               倒数切片 s[-10:-1]
               逆序 [::-1]
               隔一取一  s[::2]
               全选  s/s[:]/s[::]/s[:None]/s[None:]
            切片索引 可超过序列长度
            range(-1, 4, -1) 返回[-1,-2,-3]
    h3. BIF
        h4. 类型转换-工厂函数
            list()
            str()
            tuple()
        h4. 参数接受
            序列对象
                len()
                reversed()
                sum()
                zip()
            以上+可迭代对象  
                enumerate()
                sorted()
            以上+参数列表
                max()
                min()
        h4. 其他操作
            all(s)  返回 True 如果[所有]元素都是True
            any(s)  返回 True 如果[任一]元素为True
            s.count(x) 返回 x在S中出现的次数
            s.index(x) 返回 x 在s中的一次出现的下标 
h2. 列表|元组
    h3. list  元素可变,操作影响原表
        lis1 = [1,6,8,4,5]
        print(lis1[::-1]) # 倒序输出并切片
        
        [8, 6, 5, 4, 1]
        
        print(lis1[::2])  # 顺序输出并每2取1
        [8,5,1]
        
        * 逆序
        lis1 = [1,2,3,'aa']
        lis1.reverse()
        ['aa',3,2,1]
        
        * 列表推导式
        使用列表推导式生产一个包含10个元素的嵌套列表
        [[a] for a in range(10)]
        [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
        
        * 可变类型引用
        被引用时，改变原类型的值会导致引用对象的值也改变
        alist=[1,2,3,4]
        A = [alist]*3   # 引用alist
        alist[2]=50     # 改变alist序号为2的元素的值，这个时候A的 所以元素都改变了
        
        print(A)
        [[1,2,50,4],[1,2,50,4],[1,2,50,4]]
        
        
    h4. 操作符
        标准类型操作符
            比较操作符
            依次比较操作符
            直到一方胜出
        序列类型操作符
            []&[:]
            in & not in
            + 推荐使用list.extend(list2)
            * 
        列表解析    
    h4. 内建函数
        标准类型
            cmp() 依次判断
                同类型元素,比较值大小
                不同类型,都是数字,强制转换同类型
                一方数字, 数字总是最小
                否则按字母顺序
                一方先到达列表尾部, 另一方大
        序列类型
            len()/sum()/max()/min()
            sorted()/reversed()
            enumerated()/zip()
            list()/tuple()
        列表类型
            list.count()
            list.index()
            list.append()  追加到末尾
            list.insert(1, 'abc') 插入元素到索引为1的位置
            list1.extend(list2) 在list1末尾 添加list2的所有元素
            list.pop() 删除末尾元素并返回值
            list.pop(i) 删除指定元素值
            list.remove()
            list.sort()/list.reverse()  排序/逆序
        用于改变对象值[可变对象方法]
            无返回值
            直接修改原对象
    h3. tuple
        元素不可变, 一旦初始化不可修改,指向永远不变
        内建函数(BIF),基本同list
            tuple() 工厂函数
            tuple.count()
            tuple.index()
        特殊特性
            数字,字符串,元组 不可变
            可变:t = t+t1
            t = (1, 1, 1, 1, 0)
            t1 = (2,3,4,5)
            t2 = t+t1
            (1, 1, 1, 1, 0, 2, 3, 4, 5)
            若包含list元素
                list元素可变
                但指向list 不变
        默认集合类型
            多对象,都好分割,无明确用符号定义的
            函数返回默认为元组
            表示元组,建议总是用 圆括号


        单元素元组
            t = (1,)
            字典键值可作为元组
    h3. 拷贝
        浅拷贝
            新建一个对象
               对象类型同原对象
               内容为源对象内容的引用
            默认类型拷贝
               [:]  完全切片操作
               list(),dict() 工厂函数
               copy.copy()  copy模块
            区分
                字符串 
                    新建对象 +显示拷贝
                列表元素
                    新建对象 是复制引用

        深拷贝
            copy.deepcopy()  新建对象+全选引用
        h4. 非容器类型没有拷贝
                数字,字符串,其他'原子'类型对象浅拷贝用[完全切片操作]完成
            元组变量只包括源自类型对象
            不会进行深拷贝,只能得到浅拷贝
h2. 字符串
     操作符
         标准类型操作符
             比较操作, 按照ASCII值比较大小
         序列操作符
             + 可用于连接多个字符串
             % 或 join性能更佳
         格式化操作符(%)
             .format()  推荐
         辅助指令
             flags
                 + 正数前显示
                 - 左对齐
                 <sp> 一个空格
                 0, 数字用 0 填充
                 %, %%, 转义表示普通字符%
             width  显示宽度
             precision 小数点后精度
             typecode
             原始字符串操作符 (r/R) r'', 默认不转义
             Unicode 字符串操作符(u/U), u''

     独特特性
         特殊字符串
             转义字符 \
                \n 回车
                \t 制表符
                \\ 反斜杠
                \r 回车
          ''' ''' 多行内容
          不可变
             改变一个字符串元素, 需要新建字符串
          单引号与双引号用法相同,都表示字符串
          可相互嵌套, 字符串可看作是特殊的元组
    h3. 编码问题
        概念  1 bit(位)  =0/1-2 种可能性
              1 byte字节 8 bit, 2^8 可能
        种类:
            ASCII  美国标准
                1 个字节 8位
                英文字符 = 常见符号
            Unicode
                2个字节 16位
                字符集 世界文字字符
                变长编码方式
                    UTF-8  英文 1个字符
                         中文 3个字节
                         生僻字符 4-6字节
                    UTF-16  统一  2个字节
            汉字 GBK,GBK2312,GB18030
            计算机只能处理数字
                文本->数字
                Unicode 字符集 -> UTF-8 可变长编码方式
            UTF-8  
                3.X版本默认编码
            ASCII 2.X版本默认编码
            必须指定: #-*- coding:utf-8 -*-

     h3. BIF
        标准类型
        序列类型
        字符串类型
            input()
            工厂函数 
            str()&unicode()
        字符串BIF
            dir() 查看所有BIF
            更改显示方式
            检查
            修改
               expandtabs()
               replace('a','A')
               strip()/lstrip()/rstrip()
               split()/rsplit()/splitlines()
               分割三元组partition(str)/rpartition()
               .join()

            格式化字符串
                位置参数
                关键字参数
                下标
                对齐
                    < 左, > 右, ^ 居中
                .format()

            其他
                from string import  maketrans
                translate
                    table 参数
                    del 参数
 







