from math import log
import operator
import matplotlib.pyplot as plt


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
    del(labels[bestfeat]) #del函数解除变量对值的引用
    featval = [example[bestfeat] for example in dataset]
    unival = set(featval)
    for val in unival:
        sublabels = labels[:]
        mytree[bestlabel][val] = create_tree(splitdata(dataset,bestfeat,val),sublabels)
    return mytree

def getNumLeaf(myTree):#获取树的叶子数
    num = 0
    firststr = list(myTree.keys())[0]
    # Python3中使用LIST转换firstnode，原书使用[0]直接索引只能用于Python2
    # 对于树，每次判断value是否为字典，若为字典则进行递归，否则累加器+1
    seconddir = myTree[firststr]
    for key in seconddir.keys():
        if type(seconddir[key]).__name__ == 'dict':
            num += getNumLeaf((seconddir[key]))
        else: num+=1
    return num

def getTreedepth(myTree):#获取数据的层数
    maxnum = 0
    firststr = list(myTree.keys())[0]
    # Python3中使用LIST转换firstnode，原书使用[0]直接索引只能用于Python2
    # 对于树，每次判断value是否为字典，若为字典则进行递归，否则累加器+1
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

def plotmidtext(cntrpt, parentpt, txtstring):
    '''
    作用是计算tree的中间位置
    cntrpt起始位置,parentpt终止位置,txtstring：文本标签信息
    '''
    xmid = (parentpt[0] - cntrpt[0]) / 2.0 + cntrpt[0]
    ymid = (parentpt[1] - cntrpt[0]) / 2.0 + cntrpt[1]
    createplot.axl.text(xmid,ymid,txtstring)

def plottree(mytree,parentpt, nodetxt):
    numleaf = getNumLeaf(mytree)
    depth = getTreedepth(mytree)#好像没用到？？？
    firststr = list(mytree.keys())[0]
    cntrpt = (plottree.xOff + (1.0 + float(numleaf)) / 2.0/ plottree.totalW, plottree.yOff)# 计算子节点的坐标
    plotmidtext(cntrpt, parentpt, nodetxt)#给箭头写注释（箭头上的数字）
    plotNode(firststr, cntrpt, parentpt, decisionNode)#绘制节点
    secondstr = mytree[firststr]
    plottree.yOff = plottree.yOff - 1.0/plottree.totalD
    for key in secondstr.keys():
        if type(secondstr[key]).__name__ =='dict':
            plottree(secondstr[key], cntrpt, str(key))
        else:
            plottree.xOff =plottree.xOff + 1.0 / plottree.totalW
            plotNode(secondstr[key], (plottree.xOff, plottree.yOff), cntrpt, leafNode)
            plotmidtext((plottree.xOff, plottree.yOff), cntrpt, str(key))
    plottree.yOff = plottree.yOff + 1.0 / plottree.totalD
    #从上至下绘制树，从是否为字典划分

decisionNode = dict(boxstyle="sawtooth", fc="0.8")# 决策节点的属性。boxstyle为文本框的类型，sawtooth是锯齿形，fc是边框线粗细
# 可以写为decisionNode={boxstyle:'sawtooth',fc:'0.8'}
leafNode = dict(boxstyle="round4", fc="0.8") #决策树叶子节点的属性
arrow_args = dict(arrowstyle="<-") #箭头的属性

def createplot(intree):
    # fig = plt.figure(1, facecolor='white')
    # fig.clf()
    # createPlot.axl = plt.subplot(111, frameon=True)#frameon表示是否绘制坐标轴矩形
    # plotNode('decision_node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    # plotNode('leaf_node', (0.8,0.1), (0.5,0.8), leafNode)
    # plt.show()
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    axprops =dict(xticks=[],yticks=[])
    # createPlot.ax1为全局变量，绘制图像的句柄，subplot为定义了一个绘图，
    # 111表示figure中的图有1行1列，即1个，最后的1代表第一个图
    # frameon表示是否绘制坐标轴矩形
    createplot.axl = plt.subplot(111, frameon = False ,**axprops)
    plottree.totalW =float(getNumLeaf(intree))#树高
    plottree.totalD = float(getTreedepth(intree))#树深
    plottree.xOff = -0.5/plottree.totalW;
    plottree.yOff = 1.0;
    plottree(intree, (0.5,1.0), '')#0.5，1.0作为父节点位置
    plt.show()

def plotNode(nodetxt, centerpt, parentpt, nodetype):
    createplot.axl.annotate(nodetxt, xy=parentpt, xycoords='axes fraction', xytext=centerpt
                            , textcoords='axes fraction', va="center", ha="center", bbox=nodetype
                            , arrowprops=arrow_args)
    # nodeTxt为要显示的文本，xy是箭头尖的坐标，xytest是注释内容的中心坐标
    # xycoords和textcoords是坐标xy与xytext的说明（按轴坐标），若textcoords=None，则默认textcoords与xycoords相同，若都未设置，默认为data
    # va/ha设置节点框中文字的位置，va为纵向取值为(u'top', u'bottom', u'center', u'baseline')，ha为横向取值为(u'center', u'right', u'left')

if __name__ == '__main__':
    dataset= [[1,1,"sb"],
              [1,0,"nt"],
              [0,1,"nt"],
              [1,1,'sb'],
              [0,1,'nt']]
    # num = calcEnt(dataset)
    # print(num)
    # split = splitdata(dataset, 2, "sb")
    # print(split)
    # best = choosebestsplit(dataset)
    # print(best)
    labels = ['111', '222']
    tree = create_tree(dataset, labels)
    tree['111'][3] = 'fuck'
    print(tree)
    createplot(tree)