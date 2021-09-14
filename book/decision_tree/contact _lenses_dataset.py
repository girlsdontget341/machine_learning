import decision

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
labels = ['age', 'prescript','astigmatic','tearRate']
tree = decision.create_tree(lenses, labels)
decision.createplot(tree)