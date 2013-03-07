#! /usr/bin/env python
import timeit
setup='''
s.l = 1,1
for i in xrange(3,1002,2):
  s += (4*l + 10*(i-1))
	l += 4*(i-1)
print s
'''
print "%.3f"% timeit.Timer(setup=setup).timeit(), "s"
