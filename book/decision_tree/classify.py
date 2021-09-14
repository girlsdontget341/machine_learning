def  classify(inputtree, featlabels, testvec):#利用决策树分类(数据集，标签，测试数据）
    firststr = list(inputtree.keys())[0]
    seconddict = inputtree[firststr]
    featindex = featlabels.index(firststr)
    for key in seconddict.keys():
        if testvec[featindex] == key:
            if type(seconddict[key]).__name__ == 'dict':
                classlabel = classify(seconddict[key], featlabels, testvec)
            else: classlabel = seconddict[key]
        return classlabel

if __name__ =='__main__':
    dataset = {'hahaha': {0: 'nt', 1: {'jiuzhe': {0: 'nt', 1: 'sb'}}, 3: 'fuck'}}
    labels = ['hahaha','jiuzhe']
    o = classify(dataset, labels, [0,1])
    print(o)
