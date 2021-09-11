from os import listdir
from book.knn.appointment.book_knn1 import classify0
from numpy import *

def img2vector(filename):#把32*32的数字转化成1*1024的向量
    returnvec = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        line = fr.readline()#readline每次读取一行 、、readlines直接读取所有 以行返回列表
        for j in range(32):
            returnvec[0, 32 * i + j] = int(line[j])
    return returnvec

def handwritingtest():
    hwlabels = []
    training_file = listdir(r'trainingDigits')#返回文件夹里文件名字列表
    m = len(training_file)
    trainingmat = zeros((m,1024))
    for i in range(m):
        filenamestr = training_file[i]
        filestr = filenamestr.split('.')[0]
        classnumber = int(filestr.split('_')[0])#此处可简化为int（filenamestr.split（’_‘）[0]
        hwlabels.append(classnumber)
        trainingmat[i,:] = img2vector(r'trainingDigits/%s' %filenamestr)
    test_file = listdir(r'testDigits')
    t = len(test_file)
    error = 0.0
    for i in range(t):
        filenamestr = test_file[i]
        filestr = filenamestr.split('.')[0]
        classnumber = int(filestr.split('_')[0])
        test_vector = img2vector(r'testDigits/%s' %filenamestr)
        result = classify0(test_vector, trainingmat, hwlabels, 3)
        print("识别结果是： %d,   真正结果是：%d" %(result, classnumber))
        if(result!= classnumber):
            error +=1.0
            print("预测失败..人工智障")
        else: print("预测成功！牛啊牛啊")
    print("本次测试成功率为：",(1-(error/t))*100,"%")


if __name__ == '__main__':
    # test_vec = img2vector(r'testDigits\0_13.txt')#此处加r 保证\的作用
    # print(test_vec)
    handwritingtest()