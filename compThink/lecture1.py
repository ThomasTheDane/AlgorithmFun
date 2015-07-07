import pylab

pylab.figure(1)
pylab.plot([1,2,3],[4,5,6])
# pylab.show()

def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

lotsOfParameters2(1, e=20, b=3, a=10)