
import numpy as np
from sklearn.neighbors import KDTree

np.random.seed(0)
X = np.array([(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)])
tree = KDTree(X, leaf_size=2)
# ind：最近的3个邻居的索引
# dist：距离最近的3个邻居
# [X[2]]:搜索点
dist, ind = tree.query([(2.1,3)], k=3)

print ('ind:',ind)
print ('dist:',dist)