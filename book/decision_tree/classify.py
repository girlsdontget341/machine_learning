def  classify(inputtree, featlabels, testvec):#利用决策树分类
    firststr = inputtree.key()[0]
    seconddict = inputtree[firststr]
    featindex = featlabels.index(firststr)
    for key in seconddict.keys():
        if testvec[featindex] == key:
            if type(seconddict[key]).__name__ == 'dict':
                classlabel = classify(seconddict[key], featlabels, testvec)
            else: classlabel = seconddict[key]
        return classlabel