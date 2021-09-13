from math import log
import operator
#import matplotlib.pyplt as plt
import draw_tree

def calcEnt(dataset):#求香农熵 遍历最后一列作为数据字典的键 统计出现次数再求提高效率
    numEntry = len(dataset)
    labelcounts = {}
    for data in dataset:
        nowlabel = data[-1]#表示数组最后一个元素
        if nowlabel not in labelcounts.keys():
            labelcounts[nowlabel] = 0
        labelcounts[nowlabel] += 1
    shannonEnt = 0.0
    for key in labelcounts:
        prob = float(labelcounts[key]) / numEntry
        shannonEnt -= prob * log(prob , 2)
    return shannonEnt

def splitdata(dataset, axis, value):#划分数据集
    redataset = []
    for data in dataset:
        if data[axis] == value:
            redata = data[:axis]#[:0]没有意义
            redata.extend(data[axis+1:])#extend append区别：两个列表时，extend会变成一个包含所有元素的列表 append会把后一个整体作为前一个列表的元素
            redataset.append(redata)
    return redataset

def choosebestsplit(dataset):#选择最好划分的特征
    numofaxis = len(dataset[0]) - 1 #计算特征数量（需保证数据集最后一个不算）
    basechanooEnt = calcEnt(dataset) #计算最初熵值
    bestgain = 0.0
    bestaxis = -1.0
    for i in range(numofaxis):
        axislist = [data[i] for data in dataset]
        uniaxis = set(axislist) #set函数将列表元素去重返回无序元素集
        newEnt =0.0
        #计算信息增益率 选择熵大的
        for value in uniaxis:
            split = splitdata(dataset,i,value)
            prob = len(split)/float(len(dataset))
            newEnt += prob * calcEnt(split)
        newgain = basechanooEnt - newEnt
        if(newgain > bestgain):
            bestgain = newgain
            bestaxis = i
    return bestaxis

def majoritycnt(classlist):
    classcount = {}
    for i in classlist:
        if i not in classcount.keys():
            classcount[i] = 0
        classcount[i] += 1
    sortedclasscount = sorted(classcount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedclasscount[0][0]

def create_tree(dataset, labels):
    classlist = [example[-1] for example in dataset]
    if classlist.count(classlist[0]) == len(classlist):#类别完全相同时停止划分
        return classlist[0]
    if len(dataset[0]) == 1: #所有特征使用过后依旧不能保证类别中有唯一分组此时返回出现最多类别
        return majoritycnt(classlist)
    bestfeat = choosebestsplit(dataset)
    bestlabel = labels[bestfeat]
    mytree = {bestlabel:{}}
    del(labels[bestfeat]) #解除变量对值的引用
    featval = [example[bestfeat] for example in dataset]
    unival = set(featval)
    for val in unival:
        sublabels = labels[:]
        mytree[bestlabel][val] = create_tree(splitdata(dataset,bestfeat,val),sublabels)
    return mytree

def getNumLeaf(myTree):
    num = 0
    firststr = myTree.keys()[0]
    seconddir = myTree[firststr]
    for key in seconddir.keys():
        if type(seconddir[key]).__name__ == 'dict':
            num += getNumLeaf((seconddir[key]))
        else: num+=1
    return num

def getTreedepth(myTree):
    maxnum = 0
    firststr = myTree.keys()[0]
    seconddir = myTree[firststr]
    for key in seconddir.keys():
        if type(seconddir[key]).__name__ == 'dict':
            thisnum = 1+getNumLeaf((seconddir[key]))
        else:
            thisnum = 1
        if thisnum > maxnum: maxnum = thisnum
    return maxnum

def retrievetree(i):
    listof_tree =[{'222': {0: 'sb', 1: 'cnm', 2: 'sb', 3: 'nt', 5: 'cnm'}}]
    return listof_tree[i]

if __name__ == '__main__':
    dataset= [[1,2,"sb"],
              [1,0,"sb"],
              [3,3,"nt"],
              [3,5,'cnm'],
              [0,1,'cnm']]
    # num = calcEnt(dataset)
    # print(num)
    # split = splitdata(dataset, 2, "sb")
    # print(split)
    # best = choosebestsplit(dataset)
    # print(best)
    labels = ['111', '222']
    tree = create_tree(dataset, labels)
    print(tree)
