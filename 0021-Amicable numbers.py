#! /usr/bin/env python
from math import sqrt
def d(a):
    sum = 1
    for i in xrange(2,int(sqrt(a))):
        j = 1
        while a%i==0:
            j += 1
            a /= i
        sum *= (i**j-1)/(i-1)
    if a>1: sum *= a + 1
    return sum

sum = 0
for a in xrange(2,10000):
	   b = d(a)-a
	   if a!=b and b<10000 and a==d(b)-b:
		  sum += a + b

print sum >> 1
