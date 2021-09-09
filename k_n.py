#k_近邻算法简介
from sklearn.neighbors import KNeighborsClassifier
#训练集
x_training = [[10],[100],[1000],[10000]]
y_training = [2,3,4,5]
estimator = KNeighborsClassifier(n_neighbors=2)
estimator.fit(x_training,y_training)#fit方法训练
num = estimator.predict([[99]])#predict预测
print(num)
