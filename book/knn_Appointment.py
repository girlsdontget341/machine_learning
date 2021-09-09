from numpy import *

def file2matrix(filename):
    fr = open(filename)
    array0lines = fr.readlines()
    numberoflines = len(array0lines)
    returnmat = zeros((numberoflines,3))
    classlabelvector = []
    index = 0
