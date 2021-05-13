mplot3d之绘图集Bar plots

接口

Axes3D.bar(left, heigth, zs=0, zdir=’z’,*args,**kwargs)

添加2D柱形(Add 2D bar(s))

Argument    Description

left              柱状图在x轴左侧 (The x coordinates of the left sides of the bars)

height       柱状图高度(The height of the bars)

zs              柱形图的z坐标, 如果有有一个特例柱形将取代所有相同的z

zdir           绘制2D图形时,选择使用哪个方向(x,y or z)
 

以上关键字参数在bar()可用(Keyword arguments are passed onto bar())

返回 Path3DCollection

Bars3d