#! /usr/bin/env python
from math import sqrt
def d(a):
    t = a
    if a==1: return 0
    sum = 1
    for i in xrange(2,int(sqrt(a))):
        j = 1
        while a%i==0:
            j += 1
            a /= i
        sum *= (((i**j)-1)/(i-1))
    if a>1: sum *= (a+1)
    return sum-t

l = []
sum = 0
for a in xrange(2,10000):
	b = d(a)
	if a!=b and b<10000 and a==d(b) and b not in l:
		sum = sum+a+b
		l.append(a)
print sum
