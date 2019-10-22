h2. 字典 dict
    h3. 操作特性
        创建 = {}, 
            dict([['a','b'],['a1','b1']])={'a': 'b', 'a1': 'b1'}, {}.fromkeys(('k1','k2'), 'v')={'k2': 'v', 'k1': 'v'}
        访问: 键/值/键值对元组, dict.keys()/values()/items()
        判断key: has_key(k), in/not in, 
            dict.get(key,-1)--没有key就默认返回 -1,不指定时没有任何返回
        删除key:dict.pop(key)/popitem() 返回该条目值, 键值二元组, del dict[key]
        清空dict: dict.clear(), del dict
    h3. 常用BIF
        标准类型
            type()
            str()
            cmp()
            字典大小--键-值
        相关函数
            dict()  工厂函数
                参数为容器对象,可迭代的成对出现的对象, dict(((a,2),(3,4)))
            len()
                len(dict(((a,2),(3,4)))) = 2
            hash() 判断是否可哈希, 可(哈希)才能作为字典的键
            如:hash((1,2,3))  可哈希为: -378539185
               hash([1,2,3])  不可哈希报错TypeError为:  hash([1,2,3]) TypeError: unhashable type: 'list'
        返回可迭代器:
            dict.keys(), dict.values(), dict.items()
            dict.copy()  # 浅复制
            dict.get(k, default=) # 获取k值, 没有就返回默认值
            dict.setdefault(k, default=)
            dict.update({'a':'b'}) #更新字典{'a':'b'}
    h3. 字典排序
        有dic3 = {'A': 1, 'B': 11, 'E': 5, 'C': 3, 'F': 6, 'D': 4}
        
        按key排序
        sorted(dic3)
            ['A', 'B', 'C', 'D', 'E', 'F']
        按value排序
            sorted(dic3.values())
            [1, 3, 4, 5, 6, 11]
        # 按value值对key排序
        通过以下语句，我们告诉sorted对数字dict（其键）进行排序，并使用数字的class方法检索值来对它们进行排序-
        本质上，我们告诉它“对于数字中的每个键，请使用数字中的对应值与解决。”
        * sorted(dic4, key=dic4.__getitem__)
            ['A', 'C', 'D', 'E', 'F', 'B']   # 因为B对应的value最大，所以在升序的最后一位。
        或应用与列表推导式
        [value for (value) in sorted(dic4, key=dic4.__getitem__)]
            ['A', 'C', 'D', 'E', 'F', 'B']
        按值的降序对 key进行排序 reverse
         [value for (value) in sorted(dic4, key=dic4.__getitem__, reverse = True)]
            ['B', 'F', 'E', 'D', 'C', 'A']      # 因为A最小所以在最后一位
         [value for (value) in sorted(dic4, key=dic4.__getitem__, reverse = False)] # 默认是升序
        sorted(dic4)
            ['A', 'B', 'C', 'D', 'E', 'F']  # 仅仅是对key按升序排序
        
        # 列表推导式排序，按key降序排序并取降序对的 value
        [value for (key, value) in sorted(numbers.items(), reverse=True)]
            [6, 5, 4, 3, 11, 1]
            
        # 列表推导式，对列表按值进行排序，返回对应的key， 在dict中对key取值
        [i for (i) in sorted(dic4, key=dic4.__getitem__)]
            ['A', 'C', 'D', 'E', 'F', 'B']   # 按值的升序排序的key序列
        [dic4[i] for (i) in sorted(dic4, key=dic4.__getitem__)]
            [1, 3, 4, 5, 6, 11]   # 按值的升序排序的，值序列
        
        * key 映射排序
        # 有一个用英文key定义的数字 字典
        # 对英文月份含义按升序排序，为了将字符串与数字相关联，我们需要额外的上下文元素来正确地将它们关联。
        dic5 = dict(one='January',
                 two='February',
                 three='March',
                 four='April',
                 five='May')
        为了将字符串与数字相关联，我们需要额外的上下文元素来正确地将它们关联。首先创建一个新的dict5对象
        它仅包含字符串键和值，如果没有其他上下文，将无法按正确的顺序放置月份。
        为此，我们可以简单地创建另一个字典以将字符串映射到它们的数值，并使用该字典的__getitem__方法比较我们月份字典中的值
        numbermap = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}  # 创建一个字典以将字符串映射到它们的数值
        [dic5[k] for k in sorted(dic5,key=numbermap.__getitem__)]  # 列表推导式 按字符串映射数值对 字典 dic5 排序，按映射值顺序取出Value
        ['January', 'February', 'March', 'April', 'May']
        
        * 按每个字符串中重复字母的数量对键/值字符串进行排序，则可以定义自己的自定义方法以在已排序的key参数中使用
        有字符串str3 = 'aaaabbbaksidwiangvincamsdafbsdbhasdb'
        str3.count('a')   # 计算 a在字符中出现多少次
            9
        def repeats(string):
            # 按每个字符串中重复字母的数量对键/值字符串进行排序
            # Lower the case in the string
            string = string.lower()
            # Get a set of the unique letters
            uniques = set(string)
            # Count the max occurrences of each unique letter
            print(uniques)
            counts = [string.count(letter) for letter in uniques]
            print(f'counts:{counts}')
	  
            return max(counts)
        # 按每个value中字符重复次数排序
        sorted(dic5.values(), key=repeats, reverse=True)
        ['January', 'February', 'March', 'April', 'May']
        
## 字典操作，高级排序        
    h3. ** 字典高级排序
        现在，我们有一个字典来跟踪这些月中每个月的班级学生人数，例如
        trans = dict(January=33, February=30, March=24, April=0, May=7)
        
        def evens1st(num):
            # 如果我们要使用第一个偶数和第二个奇数来组织类大小，则可以这样定义：
            # Test with modulus (%) two
            if num == 0:
                return -2
            # It's an even number, return the value
            # 如果是偶数返回当前数
            elif num % 2 == 0:
                return num
            # It's odd, return the negated inverse
            # 如果是奇数，返回倒数(-1次方)对负数
            else:
                return -1 * (num ** -1)
        使用evens1st排序功能，可以得到以下输出
        sorted(trans.values(), key=evens1st, reverse=True)    # 班级人数多对优先，即降序，同时偶数月份优先，奇数月份其次。
        [30, 24, 33, 7, 0]
        
        同样，我们可以首先列出奇数类的大小，然后执行许多其他算法以准确地获得所需的排序。
        您可以对字典（或任何可迭代对象）使用许多其他复杂的排序方法和技巧。
        
                
    h3. 警告
        dict 按k查找,速度块, 但占内存
        list 按顺序查找,查找速度慢, 但不占内存
        key 必须是可哈希的不可变对象: 字符串,数值, 元组
        e.g: dic1 = {'(2,3,4)':1}
        
h2. 集合 set
    h3. 无序排列,元素必须可哈希,一组key集合, 所有值唯一不可重复
        如: s1 = set((12,3,123,123,12,3)), 
        s1 set([123, 3, 12])
    h3. 功能:
        成员关系测试,删除重复元素
    h3. 分类:
        set 可变集合
        frozenset 不可变集合
    h3. 创建:
        仅能用工厂函数
        set()/frozenset()
        s3 = set('abcasdasdasdasdasd') 
        s3 set(['a', 'c', 'b', 's', 'd'])
        s3.add('e')
        s3 set(['a', 'c', 'b', 'e', 'd', 's'])
        s2 = frozenset('abcasdasdasdasdasd')
        s2 frozenset(['a', 'c', 'b', 's', 'd'])
    h3. 操作符:
        标准类型: in /not in, <,<=,>,>=,!=,==
        集合类型:
            s1 frozenset(['a', 'c', 'b', 's', 'd'])
            s2 set(['a', 'c', 'b', 'e', 'd', 's'])
            并集 OR   # 包含所有set1 和set2的
                set1 | set2
                set1.union(set2)
            交集 AND  # 同时包含在set1 和set2的
                set1 & set2
                set1.intersection(set2)
            差补 C    # 包含在set1 中且不在set2
                set1 - set2
                set1.difference(set2)
            对称差分 XOR  # 两个集合差别项
                set1 ^ set2
                s1.symmetric_difference(s2)
                    frozenset(['e'])
                s2.symmetric_difference(s1)
                    set(['e'])
    h3. 常用BIF:
        添加元素: set.add(key)
        扩展元素: set.update(seq)
        删除元素: set.discard(obj)  #若存在obj,删除
        删除任一对象: set.pop()
    h3. set 与 tuple
        set 无序, 可变, 可看作无value的字典
            s3  set(['a', 'c', 'b', 'e', 'd', 's'])
        frozenset 无序, 不可变
            s2 frozenset(['a', 'c', 'b', 's', 'd'])
        tuple 有序, 不可变



