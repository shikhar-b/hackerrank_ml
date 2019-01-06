import numpy
import sys, pdb

if len(sys.argv) > 1:
    inf = open(sys.argv[1])
else:
    inf = sys.stdin

list1 = numpy.array(inf.readline().split())
list2 = numpy.array(inf.readline().split())
#pdb.set_trace()
list1 = [float(x) for x in list1[2:]]
list2 = [float(x) for x in list2[2:]]
m = numpy.corrcoef(list1, list2)[0, 1]
#y = mx+c, c = y-mx
c = numpy.mean(list2) - m*numpy.mean(list1)
print(str(m*10+c))