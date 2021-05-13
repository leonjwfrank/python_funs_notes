1,  函数线性图和时间直方图结合

import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(10)
y = x**3
plt.plot(x,y)               # 线性函数图
plt.bar(x,height=y)     # 直方图

# --------------
# 一张画布多张图
fig, ax = plt.subplots(2)
ax[0].plot(x,y)
ax[1].plot(x,y,'.',xi,yi,'.')
plt.show()


# --------------
# 中文
plt.plot([1,2,3],[4,5,6])
plt.xlabel(u"横轴")
plt.ylabel(u"纵轴")
plt.title("pythoner.com")
plt.show()