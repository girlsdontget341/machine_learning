### 获取数据集【知道 】 

  
*小数据:
    sklearn.datasets.load_*
*大数据集:
    sklearn.datasets.fetch_*
### 数据集返回值介绍【知道】 
 
    返回值类型是bunch--是一个字典类型

### 返回值的属性:

    *data：特征数据数组
    *target：标签(目标)数组
    *DESCR：数据描述
    *feature_names：特征名,
    *target_names：标签(目标值)名

### 数据集的划分【掌握】   

    sklearn.model_selection.train_test_split(arrays, *options)
    参数:
    x -- 特征值
    y -- 目标值
    test_size -- 测试集大小
    ramdom_state -- 随机数种子
    返回值:
    x_train, x_test, y_train, y_test