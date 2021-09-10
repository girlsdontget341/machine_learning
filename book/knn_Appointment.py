from numpy import *
import book_knn1
#import matplotlib.pyplot as plt
def file2matrix(filename):#文本转化为numpy
    fr = open(filename)
    arrayolines = fr.readlines() #读取文件行
    numberoflines = len(arrayolines) #获取行数
    returnmat = zeros((numberoflines,3))
     #生成[[0. 0. 0.]
     # [0. 0. 0.]
     # [0. 0. 0.]
     # ...
     # [0. 0. 0.]
     # [0. 0. 0.]
     # [0. 0. 0.]]  1000行
    classlabelvector = []
    index = 0
    for line in arrayolines:
        line = line.strip()#移除首尾空格
        listfromline = line.split('\t') #按制表符分割 返回列表
        returnmat[index, :] = listfromline[0:3]
        classlabelvector.append(int(listfromline[-1]))
        index += 1
    return returnmat, classlabelvector

def autonorm(dataset):
    minval = dataset.min(0)
    maxval = dataset.max(0)
    range = maxval - minval
    normdataset = zeros(shape(dataset))
    m = dataset.shape[0]
    normdataset = dataset - tile(minval,(m, 1) )#tile重复函数 即将minval复制1行m次
    normdataset2 = normdataset / tile(range, (m, 1))
    return normdataset2, range, minval

def datingtest():#只使用10%数据作为测试数据
    test_per = 0.10
    datingdatamat, datinglabels = file2matrix('datingTestSet2.txt')
    normmat, ranges, minval = autonorm(datingdatamat)
    m = normmat.shape[0]
    error= 0.0
    numberoftest = int(m*test_per)
    for i in range(numberoftest):
        classresult = book_knn1.classify0(normmat[i, :], normmat[numberoftest:m, :], datinglabels[numberoftest:m], 3)
        print("分类器返回预测结果为：%d ，真实结果为： %d"%(classresult, datinglabels[i]))
        if(classresult!=datinglabels[i]):
            error += 1.0
            print("本次预测失败..")
        else: print("本次预测成功！")
    print("本次使用错误率为 %f" % (error / float(numberoftest)))

def classifyperson():#约会喜欢程度预测函数
    resultlist = ["你就是个粑粑，爬！", "一般般吧，但还不配", "我要给你生猴子！"]
    per2 = float(input("你一周花（）%的时间玩游戏？"))
    per1 = float(input("你每年有（）公里数旅游？"))
    per3 = float(input("你每周有（）公升冰淇淋消费？"))
    arrtest = array([per1, per2, per3])
    datingdatamat, datinglabels = file2matrix('datingTestSet2.txt')
    normmat, ranges, minval = autonorm(datingdatamat)
    result = book_knn1.classify0((arrtest-minval)/ranges, normmat, datinglabels, 3)
    print("你获得的结果是：", resultlist[result-1])

if __name__ == '__main__':
    # datingtest()
    #画散点图
    # fig = plt.figure()
    # ax = fig.add_subplot(111) #用法见https://blog.csdn.net/qq_43411749/article/details/106864723?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link
    # ax.scatter(datingdatamat[:,1], datingdatamat[:,2], )#scatter传递坐标
    # plt.show()
    classifyperson()
