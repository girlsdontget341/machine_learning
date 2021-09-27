from numpy import *

def loadDataset(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curline = line.strip().split('\t')
        fitline = list(map(float, curline)) #map() 会根据提供的函数对指定序列做映射。(对每个curline取float值） Python3 返回迭代器需转换为list
        dataMat.append(fitline)
    return mat(dataMat)

def calculate_Eclud(vecA, vecB):#计算两向量之间的欧氏距离
    return sqrt(sum(power(vecA-vecB, 2)))

def rand_Centroid(dataSet, k):#选取随机数量k的质心
    n = shape(dataSet)[1]
    centroid = mat(zeros((k,n)))
    for j in range(n):
        minj = min(dataSet[:,j])
        rangej =float(max(dataSet[:,j])-minj)
        centroid[:,j] = minj + rangej * random.rand(k,1)
    return centroid

if __name__ == '__main__':
    data = loadDataset('testSet.txt')
    # print(data)
    centroid = rand_Centroid(data,2)
    print(centroid)
    re = calculate_Eclud(centroid[0],centroid[1])
    print(re)

