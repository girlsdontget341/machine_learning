from numpy import *
from load_data import *
from smo_simp import *
from Opt_smo import *
from SMO_platt import *
from Kernel import *
from image_recog import *

if __name__ == '__main__':
    data, label = loadDataSet('testSet.txt')
    #b, alpha = smoP(data, label, 0.6, 0.001, 40)
    testRbf()
    testDigits()