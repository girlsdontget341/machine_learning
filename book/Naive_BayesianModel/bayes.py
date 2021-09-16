from numpy import *



def loadDataset():#设置样本集和分类 0好1坏（啊这
    eglist = [['你','真','是','一个','好人','啊','宝'],
                ['我的','宝','长得','真的','好像','你','母猪','啊'],
                ['我','对','他','没有','坏','的','感觉'],
                ['你','好','普信','我','觉得','老','母猪','没有','你','一半','肥'],
                ['你','好','坏','我','好','喜欢','你','这种','普信'],
                ['我','是','迪士尼','在逃','普信','绝绝子','暴风吸入','yyds']
                ]
    classvec = [0,1,0,1,0,1]
    return eglist,classvec

def createVocallist(dataset):#整体返回一个字列表 自动去重
    vocalset = set([])
    for doc in dataset:
        vocalset = vocalset | set(doc)
    return list(vocalset)

def setofwords2vec(vocallist, inputset):#判断字典文档里每一个字 在输入文档中是否出现
    returnvec = [0] * len(vocallist)
    for word in inputset:
        if word in vocallist:
            returnvec[vocallist.index(word)] = 1
        else: print("%s 找不到啊" %word)
    return returnvec

def trainNB0(trainmatrix, traincategory): #通过计算条件概率
    numtraindocs = len(trainmatrix)
    numwords = len(trainmatrix[0])
    p_class = sum(traincategory)/float(numtraindocs)
    p0denom = 0.0
    p1denom = 0.0
    p0 = zeros(numwords)
    p1 = zeros(numwords)
    # 防止其中一个概率为0
    # p0denom = 2.0
    # p1denom = 2.0
    # p0 = ones(numwords)
    # p1 = ones(numwords)

    for i  in range(numtraindocs):
        if traincategory[i] == 1:
            p1 += trainmatrix[i]
            p1denom += sum(trainmatrix[i])

        else:
            p0 += trainmatrix[i]
            p0denom += sum(trainmatrix[i])
    p0vec = p0 / p0denom
    p1vec = p1 / p1denom
    # 防止太多很小的数向下溢出
    # p0vec = log(p0 / p0denom)
    # p1vec = log(p1 / p1denom)
    return p0vec,p1vec,p_class

def classifyNB(vec2classify, p0vec, p1vec, pclass1):#条件概率分类
    p1 = sum(vec2classify * p1vec) + log(pclass1)
    p0 = sum(vec2classify * p0vec) + log(1.0 - pclass1)
    if p1>p0:
        return 1
    else: return 0

def testNB():
    post,classes=loadDataset()
    # print(post)
    vocallist = createVocallist(post)
    # print(vocallist)
    # retrieve1 = setofwords2vec(vocallist, post[0])
    # print(retrieve1)
    trainmat = []
    for doc in post:
        trainmat.append(setofwords2vec(vocallist, doc))
    # print(trainmat)
    p0v, p1v, p_sum = trainNB0(trainmat, classes)
    # print(p0v)
    # print(p1v)
    test = ['yyds', '绝绝子', '母猪']
    this = array(setofwords2vec(vocallist, test))
    print (test ,"属于：", classifyNB(this,p0v,p1v,p_sum))

if __name__ == '__main__':
    testNB()