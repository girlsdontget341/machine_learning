



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

if __name__ == '__main__':
    post,classes=loadDataset()
    print(post)
    vocallist = createVocallist(post)
    print(vocallist)
    retrieve1 = setofwords2vec(vocallist, post[0])
    print(retrieve1)