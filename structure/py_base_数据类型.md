## 1. 数据类型的作用
    h3. 程序设计语言
        不允许存在语法歧义
        需要明确 数据含义
        对[数据]的一种划分
## 2. 标准类型
    h3. 标准数据类型--不可变类型
        Number(数字)
            int(整型)
            float(浮点型)
            bool(布尔)  True/False
            complex(复数)
    h3. 容器类型
        String(字符串)
        List(列表)
        Tuple(元组)
        Sets(集合)
        Dictionary(字典)
## 3. 标准类型操作符
    h3. 算术运算符
        + - * / 
        %(取模) 
        ** 求冥 
        // 取整除(商的整数部分)
    h3. 比较运算符
        ==, !=, >=, <=, >, <
    h3. 赋值运算符
        =, +=, -=,*=,/=,%=,**=,//=
    h3. 位运算符
        与二进制操作有关的
        &, |, ^, -, 与 或 异或,取反
        <<, >> 左移, 右移
    h3. 逻辑运算符
        and/or/not
    h3. 成员运算符
        in/not in
    h3. 身份运算符
        is/is not  两个变量引用对象是否同一个
        是否引用自同个对象
        == id(x) == id(y)    引用变量的值是否相等
## 4. 内建函数(BIF)
    type() 查询数据类型
    isinstance() 查询数据类型
    cmp(a,b)  1 a>b, -1 a<b, 0 a=b
    str()/repr()  返回对象的[字符串表示]
    dir()   查询一个[类or对象]所有属性
## 5. 数值类型
    h3. 分类
        整数类型
            0X, 0B, 0O
        浮点数类型
        复数类型
            z = a + bj
            a 实数部分 z.real
            b 虚数部分 z.imag
    h3. 关系
        整数--> 浮点数 --> 复数
        混合运算-->最宽类型
        相互转换 int(), float(), complex()
    h3. BIF
        abs()
        ceil()/floor() 
            上入整数/下舍整数  
        divmod()  
            num1/num2 返回元组
            num1%num2
        pow()
            指数运算
        round()
            四舍五入
    h3. 随机数运算
        random
        randint() 随机整数
        randrange() 范围类随机数
        uniform(x, y)  随机浮点数 [x,y]
        random()    随机浮点型
        choice()   随机序列中的一个元素
        shuffle(lst)   序列所有元素随机排序
        seed([x])
    h3. 空值
        None  特殊空值
        0 不是None  
## 6. 大型数据类型
    内置的数据结构的不同组合，可以得到更大更复杂的结构
    嵌套列表，嵌套元祖，嵌套字典等等
    元祖作为key，作为字典的key，比如地图的地标。
    
    
    