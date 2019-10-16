h2. 安装pandas
    pip install pandas, numpy, matplotlib

    import pandas as pd
    import numpy as np 
    import matplotlib.pyplot as plt

    h3. 数据序列的生成, Series方法
    s1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    print s1
    numpy list: [0 1 2 3 4 5] <type 'numpy.ndarray'>
    a   -1.365643
	b   -0.726986
	c   -0.986836	
	d    1.941801
	e   -0.764830
    dtype: float64

    h3. Series 方法对象可作为list对象操作
    print s1[0],  s1[:-3]
     -0.955498123527 
    a   -0.955498
    b    1.125502
    print pd.Series({'a':1, 'b':2, 'c':3})  #数据与下标同数
    print pd.Series({'a':1, 'b':2, 'c':3}, index=('a', 'b', 'c', 'd', 'e')) #数据与下标不同数
    dtype: float64
    a    1
	b    2
	c    3
	dtype: int64
	a    1.0
	b    2.0
	c    3.0
	d    NaN
	e    NaN
	dtype: float64
    

    h3. 一个定量数据, 复制给5个序列下标
    print pd.Series(5, index=('a', 'b', 'c', 'd', 'e'))
	dtype: float64
	a    5
	b    5
	c    5
	d    5
	e    5
	dtype: int64

	h3. 生成数据列表
	df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print df
    """
    A         B         C         D
	2013-01-01 10:10:10  2.293131  1.475191 -1.702366 -1.076148
	2013-01-02 10:10:10 -0.887372 -0.029572  0.633653  0.986684
	2013-01-03 10:10:10 -0.383257 -0.036327 -1.543034 -1.416213
	2013-01-04 10:10:10  0.199968  1.337480  0.510756 -1.630116
	2013-01-05 10:10:10  0.414897  1.257668 -2.483234 -2.318926
	2013-01-06 10:10:10 -0.275801  0.446873  0.766766  1.160759
    """
