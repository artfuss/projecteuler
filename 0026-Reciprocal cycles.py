#! /usr/bin/env python

import timeit
setup='''

def solve(n):
  d=1
	l=[]
	while True:
		while d<n: d *= 10
		if d%n == 0: return 0
		try:
			i=l.index((d/n,d%n))
			return len(l)-i
		except ValueError:
			l.append((d/n,d%n))
			d = d%n
m,a=0,0
for i in xrange(2,1000):
	x = solve(i)
	if m < x: m,a = x,i 
print a
'''

print "%.3f" % timeit.Timer(setup=setup).timeit(), "s"
