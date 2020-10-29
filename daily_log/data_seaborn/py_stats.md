# stats
	random.shuffle(x, [, random])
	该函数将x 随机放入队列sequence，随机算法为梅森旋转 Mersenne Twister

	random   随机变量发生器
		uniform within range    分布均匀
		支持分布
		uniform			# 制服
		triangular		# 三角
		lognormal		# 对数分布
		gamma			# 伽马分布
		beta			# beta 分布
		pareto			# 帕累托分布
		weibull			# 威布尔分布 
	distributions on the circle  # 圆上的分布
		circular uniform     # 圆形制服
		von mises		# 冯·米斯
# 概率公理
	设，a,b,P 是空间 P(E)某个事件E的概率，并且 P(a)=1,然后 (a,b,P)是概率空间，具有样本空间a
	活动空间b，和 概率测度P
	1，事件的概率非负实数
		P(E) <- R, P(E) >=0, 所有E属于b
		b是活动空间。遵循P(E)与更一般的度量理论，它总是有限的，分配负概率的理论使第一公理松弛

	2，统一性
	单位度量的假设，整个样本空间中至少一个基本事件将发生的概率为1
	P(a) = 1

	3, 可加性
	不相交集的任何可数序列，与互斥事件同义。 E1，E2，... 满足
    P(U(i=1,∞)Ei) = P(E1) + P(E2) + ...
	 有些专家只考虑了有限加性概率空间 ,在此空间内不相交集的任何事件发生的概率等于 他们单独发生之和




