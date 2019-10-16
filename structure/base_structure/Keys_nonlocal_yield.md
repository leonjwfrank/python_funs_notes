    import keyword
    keyword.kwlist
    
# yield
    新增在 python2.3
    NAMES = (('aaron', 8312), ('angela', 7603), ('dave', 7306), ('davina',7902), ('elliot', 7911), ('ernie', 7410), ('jess', 7912), ('jim', 7512), ('larry', 7311), ('leslie', 7808), ('melissa', 8602), ('pat', 7711), ('serena', 7003), ('stan', 7607), ('faye', 6812), ('amy', 7209), ('mona', 7404), ('jennifer', 7608),)


    def randName():
        pick = set(NAMES)
        while pick:
            yield pick.pop()    # 生成器

    i = 0
    gen1 = randName()
        while 1:
        i += 1
        if gen1:
            print(i, next(gen1), end='\n')     # 取出值，并在末尾换行，如果end = ’‘， 则不换行
        else:
            break

# nonlocal
    # 在python2.7中
    def e(x):
        def f():
            y = 1          # 此处不需要声明x是其他的变量
            x = x + y
            return x

    return f
    
    # 新增在 python3
    def e(x):
        def f():
            y = 1
            nonlocal x      # 此处声明x是其他范围的变量，python会去其他全局搜索这个变量
            x = x + y
            return x

    return f


    inc = e(2)
    print(inc())
    print(inc())