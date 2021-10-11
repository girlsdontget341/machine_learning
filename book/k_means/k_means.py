from numpy import *
import matplotlib.pyplot as plt
def loadDataset(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curline = line.strip().split('\t')
        fitline = list(map(float, curline)) #map() 会根据提供的函数对指定序列做映射。(对每个curline取float值） Python3 返回迭代器需转换为list
        dataMat.append(fitline)
    return array(dataMat)

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



def plot_scatter(clusters, centroids):
    idx0 = where(clusters[:, 0] == 0)
    idx1 = where(clusters[:, 0] == 1)
    idx2 = where(clusters[:, 0] == 2)
    idx3 = where(clusters[:, 0] == 3)
    #where函数返回的是两个数组 第一个横坐标 第二个纵坐标
    #此处画图只需取横坐标
    plt.scatter(x[idx0[0], 0].tolist(), x[idx0[0], 1].tolist(), marker='x', color='r')
    plt.scatter(x[idx1[0], 0].tolist(), x[idx1[0], 1].tolist(), marker='x', color='g')
    plt.scatter(x[idx2[0], 0].tolist(), x[idx2[0], 1].tolist(), marker='x', color='y')
    plt.scatter(x[idx3[0], 0].tolist(), x[idx3[0], 1].tolist(), marker='x', color='b')
    plt.scatter(centroids[:, 0].tolist(), centroids[:, 1].tolist(), marker='o', color='black', linewidths=10)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

if __name__ == '__main__':
    x = (loadDataset('testSet.txt'))

    # print(data)
    # centroid = rand_Centroid(data,4)
    # print(centroid)
    # re = calculate_Eclud(centroid[0],centroid[1])
    # print(re)
    centroids, clusters = k_means(x, 4)
    print(centroids)
    print("------------------")
    print(clusters)
    plot_scatter(clusters, centroids)

