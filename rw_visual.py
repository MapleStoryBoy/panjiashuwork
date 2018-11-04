import matplotlib.pyplot as plt

from RandomWalk import RandomWalk

#不断模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    re = RandomWalk(50000)
    re.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10,6))
    #point_numbers = list(range(re.num_points))
    plt.plot(re.x_values, re.y_values, linewidth=1)
    #突出起点和终点
    #plt.plot(0,0,c='green',edgecolors='none',linewidth=1)
   # plt.plot(re.x_values[-1],re.y_values[-1],c='red',edgecolors='none',linewidth=1)
    #隐藏坐标轴
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
