import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")# 决策节点的属性。boxstyle为文本框的类型，sawtooth是锯齿形，fc是边框线粗细
# 可以写为decisionNode={boxstyle:'sawtooth',fc:'0.8'}
leafNode = dict(boxstyle="round4", fc="0.8") #决策树叶子节点的属性
arrow_args = dict(arrowstyle="<-") #箭头的属性

def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.axl = plt.subplot(111, frameon=True)#frameon表示是否绘制坐标轴矩形
    plotNode('decision_node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('leaf_node', (0.8,0.1), (0.5,0.8), leafNode)
    plt.show()

def plotNode(nodetxt, centerpt, parentpt, nodetype):
    createPlot.axl.annotate(nodetxt, xy=parentpt, xycoords='axes fraction', xytext=centerpt
                            , textcoords='axes fraction', va="center", ha="center", bbox=nodetype
                            , arrowprops=arrow_args)
    # nodeTxt为要显示的文本，xy是箭头尖的坐标，xytest是注释内容的中心坐标
    # xycoords和textcoords是坐标xy与xytext的说明（按轴坐标），若textcoords=None，则默认textcoords与xycoords相同，若都未设置，默认为data
    # va/ha设置节点框中文字的位置，va为纵向取值为(u'top', u'bottom', u'center', u'baseline')，ha为横向取值为(u'center', u'right', u'left')

if __name__ == "__main__":
    createPlot()