from matplotlib import pyplot as plt
import numpy as np

'''
pyplot.plot(x,y)   绘制函数图像(曲线图，折线图）

    x = np.linspace(0,10,100)
    y = np.sin(x)
    
    plt.plot(x,y)
    plt.show()
    
    使用plot方法绘制出图像，生成的是一个对象，需要进一步使用plt.show()方法让编译器显示这个图像
    或者使用：
    plt.savefig('sin_graph.png')保存图片


如何在一张图中绘制多个曲线

    
    x = np.linspace(0,10,100)
    siny = np.sin(x)
    cosy = np.cos(x)
    plt.plot(x,siny)
    plt.plot(x,cosy)
    plt.show()
    
    只需要把所有要绘制的命令都写完之后再写show就可以了


如何设置线条颜色和样式
    
    plt.plot(x,y,color = 'red', linestyle = ':')
    只需要手动调整color和linestyle参数就可以了
    
    linestyle有四种可选项：
    ":"     --------------------------------    小虚线
    "-."    —— · —— · —— · —— · —— · —— · ——    点虚线
    "--"    —— —— —— —— —— —— —— —— —— —— ——    大虚线
    "-"     ————————————————————————————————    实线
    
    更多线条：https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html
    plt.plot(x,cosy,color = 'red',linestyle = (0,(3,1,1,1)))
    
    
    
    color有很多，可以通过直接使用名字或者使用16进制编码设置颜色
    b: blue
    g: green
    r: red
    c: cyan
    m: magenta
    y: yellow
    k: black
    w: white
    
    颜色调整：https://matplotlib.org/2.0.2/api/colors_api.html
    详细颜色：https://matplotlib.org/2.0.0/examples/color/named_colors.html



调节坐标轴范围：

    
    x = np.linspace(0,10,100)
    siny = np.sin(x)
    cosy = np.cos(x)
    plt.plot(x,siny)
    plt.plot(x,cosy,color = 'red',linestyle = (0,(3,1,1,1)))
    plt.xlim(-2,20)
    plt.ylim(0,1.5)
    
    
    可以使用plt.xlim()和plt.ylim()来调节x和y轴的取值范围
    
    
    也可以直接使用plt.axis([-1,11,-2,2])
    直接设置x和y轴的范围，axis()方法中需要传入一个列表，列表前两个数是x轴的范围，后两个数字是y轴的范围
    上一行的例子表示，x轴从-1到11，y轴从-2到2
    
    
    x = np.linspace(0,10,100)
    siny = np.sin(x)
    cosy = np.cos(x)
    plt.plot(x,siny)
    plt.plot(x,cosy,color = 'red',linestyle = (0,(3,1,1,1)))
    plt.axis([-1,11,-2,2])
    
    plt.show()



如何添加坐标轴名字（标签）


    使用plt.xlabel()和plt.ylabel()
    括号中以 “字符串” 的形式写入两个坐标轴的名字
    
    
    x = np.linspace(0,10,100)
    siny = np.sin(x)
    cosy = np.cos(x)
    plt.plot(x,siny)
    plt.plot(x,cosy,color = 'red',linestyle = (0,(3,1,1,1)))
    plt.axis([-1,11,-2,2])
    plt.xlabel('x')
    plt.ylabel('sin and cos')
    plt.show()



如何给每条曲线命名（起名字）
    
    需要在plt.plot(x,siny)这个方法内写入你想要的标签名字：
        plt.plot(x,siny, label = 'sin x')
        
    然后在plt.show()之前上：plt.legend()使用这个图示即可
    
    
    x = np.linspace(0,10,100)
    siny = np.sin(x)
    cosy = np.cos(x)
    plt.plot(x,siny,label = 'sin x')
    plt.plot(x,cosy,color = 'red',linestyle = (0,(3,1,1,1)))
    plt.axis([-1,11,-2,2])
    plt.xlabel('x')
    plt.ylabel('sin and cos')
    plt.legend()
    plt.show()
    


如何给这个图起名字呢（图表名）
    
    只需要在plt.show()之前加入：
        plt.title()，括号内以字符串的形式写入你要加进去的图表名，如：plt.title('this is sin and cos function')
    
    
    x = np.linspace(0,10,100)
    siny = np.sin(x)
    cosy = np.cos(x)
    plt.plot(x,siny,label = 'sin x')
    plt.plot(x,cosy,color = 'red',linestyle = (0,(3,1,1,1)))
    plt.axis([-1,11,-2,2])
    plt.xlabel('x')
    plt.ylabel('sin and cos')
    plt.legend()
    plt.title('This is sin and cos function')
    plt.show()
    


绘制散点图
    
    散点图只需要将plt.plot()变成plt.scatter()即可
    注意，一般散点图我们用来展示两个特征之间的关系，即，x1与x2，而非x与y
    
    
    x = np.linspace(0,10,100)
    siny = np.sin(x)
    cosy = np.cos(x)
    plt.scatter(x,siny,label = 'sin x')
    plt.scatter(x,cosy,color = 'red',linestyle = (0,(3,1,1,1)))
    plt.axis([-1,11,-2,2])
    plt.xlabel('x')
    plt.ylabel('sin and cos')
    plt.legend()
    plt.title('This is sin and cos function')
    plt.show()


    
    散点图中点的样式也是可以改变的
    
        
        iris = datasets.load_iris()
        X = iris.data[:,:2]
        Y = iris.target
        
        plt.scatter(X[Y == 0,0],X[Y == 0,1],color = 'red',marker = 'o')
        plt.scatter(X[Y == 1,0],X[Y == 1,1],color = 'blue',marker = '+')
        plt.scatter(X[Y == 2,0],X[Y == 2,1],color = 'green',marker = 'x')
        plt.show()
    
        更多样式：https://matplotlib.org/3.1.1/_modules/matplotlib/markers.html#MarkerStyle
    
    
    
    
调整透明度
    
    通过plt.scatter()中的alpha系数来调节透明度，alpha = 0 为全透明，alpha = 1 为实心
    plt.scatter(x,siny,label = 'sin x',alpha = 0)
    
    
    n = 3000
    x1 = np.random.normal(0,1,n)
    x2 = np.random.normal(0,1,n)
    plt.scatter(x1,x2,alpha = 0.3)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()
    
    调整透明度后我们发现，正中心几乎变成实心，说明很密集，这也印证了均值为0


'''

