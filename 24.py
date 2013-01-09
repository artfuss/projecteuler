#! /usr/bin/env python
l,n=362880,10**6
m=[0 for i in xrange(10)]
p=[i for i in xrange(10)]
for i in xrange(9,0,-1):
  while n - l > 0:
		n -= l
		m[i] += 1
	l /= i
import sys
for i in xrange(9,-1,-1):
	sys.stdout.write("%d"%p[m[i]])
	p.remove(p[m[i]])
