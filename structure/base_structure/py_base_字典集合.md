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



