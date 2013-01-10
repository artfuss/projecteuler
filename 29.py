#! /usr/bin/env python
import timeit
setup='''
import math
b = 100
s = (b-1)*(b-1)
for i in xrange(2,int(math.sqrt(b))+1):
  j = 2
	while i**j <= b:
		s -= b/j-2+1
		j += 1
print s+1
'''

print "%.3f" %timeit.Timer(setup=setup).timeit(), "s"
