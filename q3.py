# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np, math
from sklearn.svm import LinearSVC
import pandas as pd

file3 = 'features_data.csv'
features = open(file3, 'r')


train = []
n=0
for line in features.readlines():
    if n==0:
        n=1
        continue
    train.append([float(x) for x in line.split(',')[1:]])

train = np.array(train)
train_X = train[:,:-1]
train_Y = train[:,-1]

N = len(train_X)
limit = int(math.ceil(0.7*N))
tr_X = train_X[:limit, :]
test_X = train_X[limit:, :]

tr_Y = train_Y[:limit]
test_Y = train_Y[limit:]

clf = LinearSVC()
category = np.array(test_X)
clf.fit(np.array(tr_X), category)

T = len(test_Y)
#pdb.set_trace()
confidence = clf.decision_function(test_X)
misslassification = 0.0
for i,y in enumerate(y_preds):
    misslassification+= abs(y-test_Y[i])
print('%f missclassified'%misslassification)

