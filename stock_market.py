import datetime, time,sys, collections
import numpy as np


N = int(sys.stdin.readline())

X = {}
Test = {}
for i in range(N):
    s = sys.stdin.readline().strip().split()
    timestamp = time.mktime(datetime.datetime.strptime(s[0]+' '+s[1], "%m/%d/%Y %H:%M:%S").timetuple())
    if 'Missing' in s[2]:
        Test[int(s[2].split('Missing_')[1])] = timestamp
    else:
        X[timestamp] = float(s[2])

z = np.polyfit(list(X.keys()), list(X.values()), 3)
p = np.poly1d(z)

od = collections.OrderedDict(sorted(Test.items()))

for k,v in od.items():
    print ('%.2f'%p(v))
