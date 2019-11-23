## 1.  错误处理概述
    h3.   错误
        h4. 语法错误
        h4. 逻辑错误
    h3.   异常
        h4.   定义, 程序错误,正常控制流以外采取的行为
        h4.   两个阶段
            1,检测到错误, 解释器触发的[异常]
            2,调用不同[操作] 即[处理异常]
        h4.   常见类型
            1, BaseException
                Keyboardinterrupt 用户中断执行
                SystemExit  解释器请求退出
                Exception  
                    NameError   访问未申明变量
                    ZeroDivisionError  除零错误
                    SyntaxError  解释器语法错误
                    IndexError   索引超出序列范围
                    KeyError     访问不存在的Key
                    IOError      输入/输出错误
                    AttributeError  访问未知的对象属性
            2, 其他错误类型
                都继承自BaseException
## 2.  异常处理
    h3.   try...except...except...else...finally...
        h4.   try  
            需要检测的代码
            出现异常多层比较
            找到归属,执行语句
            语句中 异常发生点后的剩余语句,永远不会执行
        h4.   except
            语法  except Exception[as var]
            几种用法
                捕获多个异常
                    except(元组)
                捕获所有异常
                    except 空子句
                    except Exception
                    except BaseException
            捕获后忽略错误
                except exception:pass
        h4.   else
            可选
            无异常发生 执行该语句
        h4.   finally
            无论是否异常都会执行,通常用于清理.
    h3.   流程:
        try -->异常-->except-->finally
        try -->异常-->else -->finally
        try-except 捕捉异常
        try-finally 用于 维持一致行为,关闭文件,清理环境.
    h3.   补充:
        若无法将[异常]交给合适[处理器]
            如:except 后的错误类型,不符合
            同时没有 不加参数的except(捕获全部异常)
        [异常] 将继续,向上抛出
        知道 被捕捉 or 造成主程序报错
    h3.   except 错误类型
        捕获 该错误类型及所有子类
        不要处理并忽略所有,建议处理方式:
            捕获[特定异常]并忽略
            捕获[所有异常]并处理
## 3.  调试
    h3.   IPython 交互式调试器
        %debug  引发异常的栈帧,直接跳到 debug,调用调试器
        %pdb    出现异常后 直接调用调试器
        调试器中 可执行任意Python代码
                 可查看各个栈帧的对象&数据
        调试器命令
            help  命令列表
            continue 恢复程序执行
            quit  退出调试器
            break  number,该行设置断点
            step  函数调用,单步进入
            next  执行当前行,前进下一行
            args   显示当前函数参数
            切换栈级别
                up down
    h3.  其他
        h4. assert
            断言 必须为真, 发生异常判定为假
            表达式 assert expression[.arguments]
            e.g.  assert n!= 0
        h4. logging
            logging.info()  允许配置[记录信息]级别日志
            代码
                import logging   logging basicConfig(level=logging.INFO)
            级别 debug/info/warning/error
    
        h4. pdb
            让程序以[单步方式]运行
            程序
                以参数 -m pdb 启动
                输入命令:
                    单步执行代码  n
                    查看变量 p
                    退出程序,结束调试  q
        h4.   pdb.set_trace()
            import pdb 
            # 可能出错的地方设置一个断点
                pdb.set_trace()
            命令:
                查看变量 P
                继续运行 C

## 3.  补充
    h3.   上下文管理 with   
        语法 with context as f:
                f.suite
        原理:
            执行完 with内的代码块
            恢复到执行前的状态
        保证文件可关闭 with open(path) as f:
                           for Line in f:
    h3.  抛出异常:
        raise Exception('')
        raise 当前错误,原样抛出,不带参数
        获取异常信息:
            sys.exc_info()


