from numpy import *
import  operator
group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
labels = ['A', 'A', 'B', 'B']
def classify0(inX, dataset, labels, k):
    datasetsize= dataset.shape[0]
    print(datasetsize)
    diffmat = tile(inX, (datasetsize, 1)) - dataset
    sqdiffmat = diffmat**2
    sqdistances = sqdiffmat.sum(axis=1)
    distances= sqdistances**0.5
    sorteddisindices= distances.argsort()#从小到大返回索引值
    print(sorteddisindices)
    classcount ={}
    for i in range(k):
        voteilabel = labels[sorteddisindices[i]]
        #print(voteilabel)
        classcount[voteilabel]= classcount.get(voteilabel, 0) + 1
        print(classcount[voteilabel])
    sortedclasscount =sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
    #.items()将字典变对应元组列表
    #itemgetter定义函数，获取对象的第1个域的值
    #reverse降序
    #获得最近3个哪类出现的次数多 即属于哪类
    print(sortedclasscount[0][0])
    return sortedclasscount[0][0]
if __name__ == '__main__':
    classify0([0,0], group, labels, 3)

