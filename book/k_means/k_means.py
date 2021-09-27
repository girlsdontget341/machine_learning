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

def k_means(dataSet,k):
    m = list(shape(dataSet))[0]
    cluster = mat(zeros((m, 2)))#cluster用来储存簇信息 第一列索引 第二列点到质心误差
    centroids = rand_Centroid(dataSet, k)#随机初始化质心
    clusterChanged = True#设置一个bool值 记录簇质心是否改变
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = calculate_Eclud(centroids[j,:],dataSet[i,:])#通过计算欧式距离找到最优的质心
                if distJI<minDist:
                    minDist = distJI
                    minIndex = j
            if cluster[i,0] != minIndex:
                clusterChanged=True
            cluster[i,:] = minIndex, minDist**2
        # print(centroids)
        for cent in range(k):#选取同一簇附近点的平均值作为质心
            ptsinCent = dataSet[nonzero(cluster[:,0].A == cent)[0]]
            centroids[cent,:] = mean(ptsinCent, axis=0)
    return centroids, cluster

if __name__ == '__main__':
    data = mat(loadDataset('testSet.txt'))
    # print(data)
    # centroid = rand_Centroid(data,4)
    # print(centroid)
    # re = calculate_Eclud(centroid[0],centroid[1])
    # print(re)
    centroids, clusters = k_means(data, 4)
    print(centroids)
    print("------------------")
    print(clusters)
