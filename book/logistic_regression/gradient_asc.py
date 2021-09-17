from numpy import *

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

if __name__ == '__main__':
    dataarr, labelmat = loadDataset()
    a = gradientasc(dataarr, labelmat)
    print(a)