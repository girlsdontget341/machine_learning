import random
import re
import bayes
def textparse(bigstring):#利用正则表达式分割去除表达符号
    listoftokens = re.split(r'\W*', bigstring)
    return [tok.lower() for tok in listoftokens if len(tok)>2]#去除空字符串 .lower()全部换为小写

def spamTest():
    doclist = []
    classlist = []
    fulltext = []
    for i in range(1,26):#分别遍历邮件 分为两类 1垃圾 0不垃圾
        wordlist = textparse(open('email/spam/%d.txt' %i).read())
        doclist.append(wordlist)
        fulltext.extend(wordlist)
        classlist.append(1)
        wordlist = textparse(open('email/ham/%d.txt' % i).read())
        doclist.append(wordlist)
        fulltext.extend(wordlist)
        classlist.append(0)
    vocallist = bayes.createVocallist(doclist)#创建词汇表
    trainset = list(range(50))#利用随机数 选择10个作为测试集
    testset = []
    for i in range(10):
        randinex = int(random.uniform(0,len(trainset)))
        testset.append(trainset[randinex])
        del(trainset[randinex])#从训练集中删除10个测试集

    #一下同bayes.py中分类步骤
    trainmat =[]
    trainclass = []
    for docindex in trainset:
        trainmat.append(bayes.setofwords2vec(vocallist, doclist[docindex]))
        trainclass.append(classlist[docindex])
    p0v,p1v,p_sum=bayes.trainNB0(trainmat,trainclass)
    error=0.0
    for docindex in testset:
        wordvector = bayes.setofwords2vec(vocallist, doclist[docindex])
        if bayes.classifyNB(wordvector, p0v, p1v, p_sum) != classlist[docindex]:
            error += 1.0
    print(len(testset))
    print('the error rate is ', float(error)/len(testset))

if __name__ == '__main__':
    spamTest()
