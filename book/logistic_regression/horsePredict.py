from numpy import *
import gradient_asc

def classifyVector(inx, weights): #分类函数
    prob = gradient_asc.sigmoid(sum(inx*weights))
    if prob>0.5:
        return 1.0
    else: return 0.0

def colicTest():
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    training = []; trainingLabels= []
    for line in frTrain.readlines():
        currline = line.strip().split('\t')
        linearr = []
        for i in range(21):
            linearr.append(float(currline[i]))
        training.append(linearr)
        trainingLabels.append(float(currline[21]))
    trainweights = gradient_asc.stocgradasc1(training, trainingLabels, 500)
    error = 0;
    numTest = 0.0
    for line in frTest.readlines():
        numTest += 1.0
        currline = line.strip().split('\t')
        linearr = []
        for i in range(21):
            linearr.append(float(currline[i]))
        if int(classifyVector(linearr, trainweights)) != int(currline[21]):
            error += 1
    errorrate  = float(error)/numTest
    print("预测错误率为： ", errorrate)
    return errorrate

def multitest():
    num = 10
    errorsum = 0.0
    for k in range(num):
        errorsum += colicTest()
    print("在 %d次迭代后" %num,"平均错误率为： %f" %(errorsum/float(num)))

if __name__ == '__main__':
    multitest()