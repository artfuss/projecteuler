#! /usr/bin/env python

def solutions(p):
  s = 0
	for a in xrange(1,p/2):
		if (p*(p-2*a)) % (2*(p-a)) == 0:s += 1
	return s/2+1 if s%2 else s/2
m,s = 0,0
for p in xrange(1,1001):
  x = solutions(p)
	if m < x: m,s = x,p

print s
