h2. 模块概述
    h3. 目的
        从[逻辑]上组织代码
        包含Python对象定义, 语句
    h3. 一个.py文件构成一个模块
        可调用其他文件中的程序
    h3. 模块的引入

    h3. 搜索路径

    h3. BIF
   
h2. 包
    h3. 模块与包 的含义
       组织py代码, .py文件
       组织模块, 包含 __init__.py 的文件夹
    h3. 含义:
        分层次文件目录结构
            模块, 子包,子子包
        [功能相似的模块]组成
        每个子包/包都含有__init__.py
            初始化文件,导入时必须,可以是空文件
            用于标识当前文件夹是一个[package]
    h3. 访问: 句点属性标识符
        如: a.b
    h3. 导入:
        import
        绝对导入
        相对导入  不推荐
h2. 名称空间
    h3. 字典
        变量名称, 对象的[关系映射集合]
    h3. 载入顺序
        __builtins__  内建名称空间
        全局名称空间
        局部名称空间
    h3. 名称查找
        与载入顺序相反
        局部变量会覆盖全局变量
    h3. 使用名称空间
        任何需要放置数据的地方
        如:函数: func.attribute
        模块: module.attribute
        类(实例):obj.attribute


h2. 标准文件模板
    h3. 两行标准注释
    #!/usr/bin/env python
    # _*_ coding:utf-8 _*_
    h3. 模块说明,作者和时间
    """
    module __doc__
    """
    __author__


h2. 作用域
    h3. 正常变量
        公开可直接引用 public
        abc,123, PI
    h3. 特殊变量
        有特殊用途, 但也可直接被引用
        __xxx__,如模块定义的文档注释 __doc__
    h3. 私有变量
        不应该直接引用,private
        __abc, _abc
        目的
        代码封装和抽象
            private, 外部不需要引用的
            public, 外部需要引用的函数
h2. 其他
    h3. 模块的安装工具, Python 内部已封装 pip, easy_install
    h3. 导入技巧:
        别名及导入模块的技巧
        目的:优先导入某模块, 没有该模块时, 降级使用另一模块
            try:
                import cString as StringIO
            except ImportError:
                import StringIO
        String 已合并到IO, 如果没有该模块,StringIO总是可用
    h3. 运行
        运行时, python 解释器把特殊变量__name__ 设为__main__
        在其他地方导入该模块时, if 将判定失败
        if __name__ == "__main__":
            test()
        if 测试目的
            让一个模块运行时正常
        使用__future__
        把下一个新版本特性导入到当前版本
            from __future__ import division




