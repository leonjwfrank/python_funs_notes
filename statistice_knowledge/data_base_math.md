## 数据基础算法 六种
    
### 朴素贝叶斯分类器(Naive Bayes classifier)
    P(A|B) = P(B|A)P(A) / P(B)

### 线性回归
    最小二乘，使残差平方和最小化
    y = a0 + a1x1 + a2x2 + ... + anxn
    
### 逻辑回归(Logistic regression)
    二元分类，输出结果只有两种情况的概率
    归一化
    sigmoid，relu 等法
    
### 神经网络(Neural Networks)
    卷积神经 神经网络，前馈神经网络，递归神经网络
    RELU, sigmoid, 双曲正切函数
    
### K-平均 聚类(K-Means Clustering)
    无监督学习算法，用于对未标记数据进行分类
    集合中任意两个元素对距离概念：
        d((x1,y1),(x2,y2)) = √(x2-x1)**2 + (y2-y1)**2
        欧式距离
        曼哈顿距离(出租车距离)
    
### 决策树
    类似流程图对树结构，使用分支方法说明决策对每个可能结果
    依赖信息论(information theory)
    信息论中，人对某个主题了解越多，新信息就知道的越少，
    关键是熵(entropy)，一种变量不确定的度量
        entropy = - ∑ P(xi)log_b * P(xi)
        P(x) 是数据集特征出现的概率
        b是对数函数低，如2，e，10
        
### NLP自然语言处理
    分词
    切词