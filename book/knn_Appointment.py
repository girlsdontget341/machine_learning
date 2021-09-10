from numpy import *
import matplotlib.pyplot as plt
def file2matrix(filename):
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
if __name__ == '__main__':
    datingdatamat, datinglabels = file2matrix('datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111) #用法见https://blog.csdn.net/qq_43411749/article/details/106864723?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link
    ax.scatter(datingdatamat[:,1], datingdatamat[:,2], )#scatter传递坐标
    plt.show()