#! /usr/bin/env python

import timeit
setup='''
m,n = 3,2
sum,min = 0,0
a,b=0,0
for m in xrange(3,10**3):
	for n in xrange(2,10**3):
		sum = (m*(m+1)/2)*(n*(n+1)/2)
		if abs(2*10**6-min) > abs(2*10**6-sum): 
			min = sum
			a,b = m,n

print a*b
'''
print timeit.Timer(setup=setup).timeit()
