## 1. 模块概述
    h3. 目的
        从[逻辑]上组织代码
        包含Python对象定义, 语句
    h3. 一个.py文件构成一个模块
        可调用其他文件中的程序
    h3. 模块的引入

    h3. 搜索路径

    h3. BIF

## 2. 包
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
## 3. 名称空间
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


## 4. 标准文件模板
    h3. 两行标准注释
    #!/usr/bin/env python
    # _*_ coding:utf-8 _*_
    h3. 模块说明,作者和时间
    """
    module __doc__
    """
    __author__


## 5. 作用域
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
## 6. 其他
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


## 7. 标准库
    1，数字和数学模块
    numbers:数字抽象基类 
    math:数学函数 
    cmath:复数的数学函数 
    decimal:十进制定点和浮点算术 
    fractions:有理数 
    random:生成伪随机数 
    statistics:数学统计功能
    
    2. 数据类型
    数据类型
    datetime:基本日期和时间类型 
    calendar:与日历相关的一般功能 
    collections:容器数据类型 
    heapq:堆队列算法 
    bisect:数组二分算法 
    array:高效的数值数组 
    weakref:弱引用 
    types:动态类型创建和内置类型的名称 
    copy:浅层和深层复制操作 
    pprint:格式化输出 
    reprlib:备用repr()实现
    enum :支持枚举
    
    3. 功能编程模块 
    itertools:为高效循环创建迭代器的函数 
    functools:可调用对象的高阶函数和操作 
    operator:标准运算符作为函数
    
    4. 数据持久化
    pickle:Python对象序列化 
    copyreg:注册pickle支持功能 
    shelve:Python对象持久化 
    marshal:内部Python对象序列化 
    dbm:与Unix“数据库”的接口 
    sqlite3:SQLite数据库的DB-API 2.0接口
    
    5. 数据压缩和存档
    zlib:与gzip兼容的压缩 
    gzip/bz2:支持gzip/bzip2文件 
    lzma:使用LZMA算法进行压缩 
    zipfile:使用ZIP存档 
    tarfile:读取和写入tar归档文件
    
    6. 文件格式
    csv:CSV文件读写 
    configparser:配置文件解析器 
    netrc:netrc文件处理 
    xdrlib:对XDR数据进行编码和解码 
    plistlib:生成并解析Mac OS X.plist文件
    
    7. 文件和目录访问
    pathlib:面向对象的文件系统路径 
    os.path:常见的路径名操作 
    fileinput:迭代多个输入流中的行 
    stat:解释stat()结果 
    filecmp:文件和目录比较 
    tempfile:生成临时文件和目录 
    glob:Unix样式路径名模式扩展 
    fnmatch:Unix文件名模式匹配 
    linecache:随机访问文本行 
    shutil:高级文件操作 
    macpath:Mac OS 9路径操作函数
    
    8. 通用操作系统服务
    os:其他操作系统接口
    io:用于处理流的核心工具
    time:时间访问和转换 
    argparse:用于命令行选项，参数和子命令的解析器 
    getopt:用于命令行选项的C风格解析器 
    logging:Python的日志记录工具 
    getpass:便携式密码输入 
    curses:字符单元格显示的终端处理 
    platform:访问底层平台的标识数据 
    errno:标准errno系统符号 
    ctypes:Python的外部函数库
    
    9.并发执行
    threading:基于线程的并行性
    multiprocessing:基于进程的并行性 
    concurrent.futures:启动并行任务 
    subprocess:子流程管理 
    sched:事件调度程序 
    queue:同步的队列类 
    _thread:低级线程API
    
    10. 加密服务
    hashlib:安全哈希和消息摘要算法接口 
    hmac:用于消息身份验证的密钥哈希算法 
    secrets:生成用于管理机密的安全随机数
    
    11.网络和进程间通信
    asyncio:异步I/O 
    socket:低级网络接口 
    ssl:套接字对象的TLS/SSL包装器 
    select:等待I/O完成 
    selectors:高级I/O复用 
    asyncore:异步套接字处理程序 
    asynchat:异步套接字命令/响应处理程序 
    signal:设置异步事件的处理程序 
    mmap:内存映射文件支持
    
    12.互联网数据处理
    email:电子邮件和MIME处理包 
    json:JSON编码器和解码器 
    mailcap:Mailcap文件处理 
    mailbox:以各种格式处理邮箱 
    mimetypes:将文件名映射到MIME类型 
    base64:Base16/Base32/Base64/Base85数据编码 
    binhex:对binhex4文件进行编码和解码 
    binascii:在二进制和ASCII之间转换 
    quopri:对MIME引用的可打印数据进行编码和解码 
    uu:对uuencode文件进行编码和解码
    
    13.互联网协议和支持
    webbrowser:Web浏览器控制器 
    cgi:通用网关接口支持 
    cgitb:CGI脚本的回溯管理器 
    wsgiref:WSGI实用程序和参考实现 
    urllib:URL处理模块
    http:HTTP模块 
    ftplib/poplib/imaplib/nntplib/smtplib: FTP/POP3/IMAP4/NNTP/SMTP协议客户端 
    smtpd:SMTP服务器 telnetlib:Telnet客户端 
    socketserver:网络服务器的框架 
    xmlrpc:XMLRPC服务器和客户端模块
    ipaddress:IPv4/IPv6操作库
    
    14.多媒体服务
    audioop:处理原始音频数据 
    aifc:读写AIFF和AIFC文件 
    sunau:读取和写入Sun AU文件 
    wave:读写WAV文件 
    chunk:读取IFF分块数据 
    colorsys:颜色系统之间的转换 
    imghdr:确定图像的类型 
    sndhdr:确定声音文件的类型 
    ossaudiodev:访问兼容OSS的音频设备
    
    15.结构化标记处理工具 
    html:超文本标记语言支持
    xml:XML处理模块
    
    16. 程序框架
    turtle — 海龟作图库
    cmd —支持面向行的命令解释器 
    shlex —简单的词法分析
    
    17. 图形用户界面 
    tkinter:Tcl/Tk的Python接口
    
    18. 命名空间(namespace)
    表示标识符(identifier)的可见范围
    一个标识符可以在多个命名空间中定义，在 不同命名空间中的含义互不相干
    dir(<名称>)函数:列出名称的属性 help(<名称>)函数:显示参考手册
    
## 8, PIL 图形处理和图形信息隐藏工具
    轻微改变图片中像素的RGB值，肉眼无法查看
    8bit R/G/B中的最低1bit，用于隐藏一个数据文件（如文本）
        每3个像素可以隐藏1个字节
        使用不失真的图像格式
    要求:
        工具1，提供图片和数据文件，生成隐藏信息的图片
        工具2，从隐藏信息的图片中提取数据信息
