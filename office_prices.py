import sys, pdb
import numpy as np
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression


if len(sys.argv) > 1:
    inf = open(sys.argv[1])
else:
    inf = sys.stdin

poly = PolynomialFeatures(degree = 1)
lin_regressor = LinearRegression()

line1 = inf.readline()
line1 = line1.split(' ')
D = int(line1[0])
N = int(line1[1])
train = []
for i in range(N):
    train.append([float(x) for x in inf.readline().split(' ')])

train = np.array(train)
train_X = train[:,:-1]
train_Y = train[:,-1]

#pdb.set_trace()
train_X_transformed = poly.fit_transform(train_X)
lin_regressor.fit(train_X_transformed,train_Y)

T = int(inf.readline())
test = []
for i in range(T):
    test.append([float(x) for x in inf.readline().split(' ')])

#pdb.set_trace()
test = np.array(test)
test_X_transformed = poly.fit_transform(test) 
y_preds = lin_regressor.predict(test_X_transformed)
for y in y_preds:
	print(str(y))