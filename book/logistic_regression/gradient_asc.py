from numpy import *
import matplotlib.pyplot as plt

def loadDataset():#加载数据
    datamat = []
    labelmat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        datamat.append([1.0, float(lineArr[0]), float(lineArr[1])])#令X0为1.0 ，同X1，X2组成3*100数组
        labelmat.append(int(lineArr[2]))#储存类别
    return datamat, labelmat

def sigmoid(inx):#海维赛德阶跃函数 输出01之间
    return 1.0/(1+exp(-inx))

def gradientasc(datamatin, classlabels):#梯度上升法求权重（回归系数）
    datamatrix = mat(datamatin)
    labelmat = mat(classlabels).transpose()#转置成列向量方便计算
    m, n = shape(datamatrix)
    alpha = 0.001#移动步长
    maxcycles = 500#迭代次数
    weights = ones((n, 1))
    for k in range(maxcycles):
        h = sigmoid(datamatrix * weights)
        error = (labelmat - h)#此处计算真实类别，与预测类别之间的差距，利用差值预测调整回归系数
        weights = weights + alpha * datamatrix.transpose() * error
    return weights

def plotfit(weights):
    dataarr, labelmat = loadDataset()
    dataArr = mat(dataarr)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelmat[i]) == 1 :
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #scatter为画散点图的函数（x, y, s, c, marker)(横坐标，纵坐标， 散点大小， 颜色，散点形状）
    ax.scatter(xcord1, ycord1, s=30 ,c='blue', marker = 's')
    ax.scatter(xcord2, ycord2, s=30, c='green' )
    # arange函数生成一个指定起点终点和步长的列表，参数个数最多三个：
    # 分为一个参数，两个参数，三个参数三种情况
    # 1.一个参数时，参数值为终点，起点取默认值0，步长取默认值1。
    # 2.两个参数时，第一个参数为起点，第二个参数为终点，步长取默认值1。包前不包后
    # 3.三个参数时，第一个参数为起点，第二个参数为终点，第三个参数为步长；步长支持小数。
    x = arange(-3.0, 3.0, 0.1)
    # z=w0x0+w1x1+w2x2
    # x0默认为1
    # 在sigmoid函数中 0被认为是0，1两类的分界处 即z=0 此处y即X2
    y = (-weights[0] - weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


if __name__ == '__main__':
    dataarr, labelmat = loadDataset()
    a = gradientasc(dataarr, labelmat)
    print(a)
    plotfit(a.getA())