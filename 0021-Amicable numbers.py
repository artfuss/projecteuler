#! /usr/bin/env python

def d(a):
  sum = 0
	for i in xrange(1,a):
		if a%i==0: sum+=i
	return sum

l = []
sum = 0
for a in xrange(1,10000):
	b = d(a)
	if a!=b and b<10000 and a==d(b) and b not in l: 
		sum = sum+a+b
		l.append(a)

print sum
