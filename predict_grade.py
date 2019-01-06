import json, sys
from sklearn.feature_extraction import DictVectorizer
import numpy as np

def cos_sim(a, b):
	"""Takes 2 vectors a, b and returns the cosine similarity according
	to the definition of the dot product
	"""
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)

v = DictVectorizer(sparse=False)


file = open('training-and-test/training.json')


N = int(file.readline())
train = []
label = []
for i in range(N):
    marks = json.loads(file.readline())
    if 'Mathematics' in marks:
        del marks['serial']
        label.append(marks['Mathematics'])
        del marks['Mathematics']
        train.append(marks)

X = v.fit_transform(train)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X, label)

test_file = open('training-and-test/sample-test.in.json')
#test_file = sys.stdin
T = int(test_file.readline())
predict =[]
vect = []
for i in range(T):
    marks = json.loads(test_file.readline())
    del marks['serial']
    vect.append(v.transform(marks)[0])

    # sim = 0
    # id = 0
    # for idx,ent in enumerate(X):
    #     val = cos_sim(ent, vect[0])
    #     if val > sim:
    #       id = idx
    #       sim = val
predict = classifier.predict(vect)

opt = open('grades_opt.txt','w+')
for g in predict:
    opt.write(str(g)+'\n')
opt.close()



