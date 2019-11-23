## 文件处理
    h3. 文件对象
        访问 普通磁盘文件
             类文件, 如:通过URL读取的Web页面
        h4. 内建函数 
            open()
                含义
                    提供初始化输入/输出操作通用接口, 返回文件对象或引发一个错误
                    f = open(''.txt, 'r')
                    f.seek(0) # 指针移到开始位置
                参数 access_mode # b+ 表示二进制读写模式
                     r/w/a  #读写追加
                     r+  #文件指针在文件开头
                     w+  #文件覆盖已存在, 创建不存在
                     a+  #文件指针在文件尾部
                返回 file 对象
        h4. 内建方法
            输入: file.read(size)  #size 为字节数, 无参数时, 一次性读取
                readline()/readlines()
                xreadlines()  #每次读取一块, 减少内存占用
            输出:  write(), writelines()
            字节偏移量文件定位: file.seek(0) #移到文件指针
                file.tell()
            其他操作:
                f.close()
                f.flush()  # 内部缓冲区数据立即写入文件
                f.truncate() #截取到当前指针位置 或 给定size, 若刚打开即调用函数,文件被删除(从0开始截取)
        h4. 内建属性
            f.closed()  #返回 True/False
            f.encoding
            f.mode    #访问模式
            f.name

    h3. 文件迭代
        自身作为[迭代器]
             for Line in open(*.txt)
             file.next()
        文件迭代更高效,更简洁
        老方法: #更占内存
            f.readline()/f.readlines()

    h3. 标准文件对象
        标准输入
            stdin
                键盘, input() 从sys.stdin 接受输入
        标准输出
            stdout            
                到显示器的缓冲输出,print 输出到sys.stdout
        标准错误
            stderr
               到显示器的非缓冲输出

    h3. 分隔符
        行分隔符
            POSIX(Unix/Mac OS X)  \n
            DOS  \r\n
        路径分隔符
            POSIX(Unix/Mac OS X) /
            DOS  \
        跨平台
            import os
            属性:
                os.sep #路径 '\\'
                os.linesep  # 行分隔符 '\r\n'
                os.pathsep  # 路径分隔符 ','
                os.curdir   # 当前工作目录  字符串表示 '.'
                os.pardie   # 父目录    '_'


