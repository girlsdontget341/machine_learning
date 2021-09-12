from math import log

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

if __name__ == '__main__':
    dataset= [[1,2,"sb"],
              [1,0,"sb"],
              [3,3,"nt"]]
    # num = calcEnt(dataset)
    # print(num)
    # split = splitdata(dataset, 2, "sb")
    # print(split)
    best = choosebestsplit(dataset)
    print(best)