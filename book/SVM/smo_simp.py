
from numpy import *
from load_data import *

def smoSimple(dataMat,classLabels,C,toler,maxIter):
    '''
    @dataMat    ：数据列表
    @classLabels：标签列表
    @C          ：权衡因子（增加松弛因子而在目标优化函数中引入了惩罚项）
    @toler      ：容错率
    @maxIter    ：最大迭代次数
    '''
    #将列表形式转为矩阵或向量形式
    dataMatrix=mat(dataMat);labelMat=mat(classLabels).transpose()
    #初始化b=0，获取矩阵行列
    b=0;m,n=shape(dataMatrix)
    #新建一个m行1列的向量
    alphas=mat(zeros((m,1)))
    #迭代次数为0
    iters=0
    while(iters<maxIter):
        #改变的alpha对数
        alphaPairsChanged=0
        #遍历样本集中样本
        for i in range(m):
            #计算支持向量机算法的预测值
            fXi=float(multiply(alphas,labelMat).T*\
            (dataMatrix*dataMatrix[i,:].T))+b
            #计算预测值与实际值的误差
            Ei=fXi-float(labelMat[i])
            #如果不满足KKT条件，即labelMat[i]*fXi<1(labelMat[i]*fXi-1<-toler)
            #and alpha<C 或者labelMat[i]*fXi>1(labelMat[i]*fXi-1>toler)and alpha>0
            if(((labelMat[i]*Ei < -toler)and(alphas[i] < C)) or \
            ((labelMat[i]*Ei>toler) and (alphas[i]>0))):
                """
                对于条件((labelMat[i]*Ei < -toler) and (alphas[i] < C))：
                αi<C,即对于边界上或边界外的点，
                当yi=1时,labelMat[i]*Ei=yi(wxi+b-yi)=f(i)-1<-toler，f(i)<1-toler；当yi=-1时，f(i)>-1+toler
                也就是边界以外的点xi经过wxi+b分类后得到的结果超出了设置的容错率，即分类错误，需要继续优化
                同理，对于条件((labelMat[i]*Ei > toler) and (alphas[i] > 0))：
                当yi=1时，labelMat[i]*Ei=yi(f(i)-yi)=f(i)-1>toler,即f(i)>toler+1；当yi=-1时，f(i)<-1-toler,说明样本i是边界外的点。
                那么αi，也就是样本i对优化目标限制条件的贡献应该为零，而条件alphas[i]>0却使样本i对限制条件的贡献大于零，说明αi是不对的，需要继续优化。
                """
                #随机选择第二个变量alphaj
                j = selectJrand(i,m)
                #计算第二个变量对应数据的预测值

                fXj = float(multiply(alphas,labelMat).T*(dataMatrix*\
                            dataMatrix[j,:].T)) + b
                #计算与测试与实际值的差值
                Ej = fXj - float(labelMat[j])
                #记录alphai和alphaj的原始值，便于后续的比较
                alphaIold=alphas[i].copy()
                alphaJold=alphas[j].copy()
                #如何两个alpha对应样本的标签不相同
                # L和H用于将alphas[j]调整到0-C之间。如果L==H，就不做任何改变，直接执行continue语句
                # labelMat[i] != labelMat[j] 表示异侧，就相减，否则是同侧，就相加。
                if(labelMat[i]!=labelMat[j]):
                    #求出相应的上下边界
                    L=max(0,alphas[j]-alphas[i])
                    H=min(C,C+alphas[j]-alphas[i])
                else:
                    L=max(0,alphas[j]+alphas[i]-C)
                    H=min(C,alphas[j]+alphas[i])
                if L==H: print("L==H");continue
                #根据公式计算未经剪辑的alphaj
                #------------------------------------------
                # eta是alphas[j]的最优修改量，如果eta==0，需要退出for循环的当前迭代过程
                # 参考《统计学习方法》李航-P125~P128<序列最小最优化算法>
                eta=2.0*dataMatrix[i,:]*dataMatrix[j,:].T-\
                    dataMatrix[i,:]*dataMatrix[i,:].T-\
                    dataMatrix[j,:]*dataMatrix[j,:].T
                #如果eta>=0,跳出本次循环
                if eta>=0:print("eta>=0"); continue
                alphas[j]-=labelMat[j]*(Ei-Ej)/eta
                alphas[j]=clipAlpha(alphas[j],H,L)
                #------------------------------------------    
                #如果改变后的alphaj值变化不大，跳出本次循环    
                if(abs(alphas[j]-alphaJold)<0.00001):print("j not moving\
                enough");continue
                #否则，计算相应的alphai值
                alphas[i]+=labelMat[j]*labelMat[i]*(alphaJold-alphas[j])
                #再分别计算两个alpha情况下对于的b值
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]\
                 *dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*\
                 dataMatrix[i,:]*dataMatrix[j,:].T
                b2=b-Ej-labelMat[i]*(alphas[i]-alphaIold)*\
                    dataMatrix[i,:]*dataMatrix[j,:].T-\
                    labelMat[j]*(alphas[j]-alphaJold)*\
                    dataMatrix[j,:]*dataMatrix[j,:].T
                #如果0<alphai<C,那么b=b1
                if(0<alphas[i]) and (C>alphas[i]):b=b1
                #否则如果0<alphai<C,那么b=b1
                elif (0<alphas[j]) and (C>alphas[j]):b=b2
                #否则，alphai，alphaj=0或C
                else:b=(b1+b2)/2.0
                #如果走到此步，表面改变了一对alpha值
                alphaPairsChanged+=1
                print("iters: %d i:%d,paird changed %d" %(iters,i,alphaPairsChanged))
        #最后判断是否有改变的alpha对，没有就进行下一次迭代
        if(alphaPairsChanged==0):iters+=1
        #否则，迭代次数置0，继续循环
        else:iters=0
        print("iteration number: %d" %iters)
    #返回最后的b值和alpha向量
    return b,alphas