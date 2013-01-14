#! /usr/bin/env python

def gcd(a,b):
  while(b):
		a,b=b,a%b
	return a

def reduce(n,d):
	u,v = n/10,n%10
	w,x = d/10,d%10
	_n = n/gcd(n,d)
	_d = d/gcd(n,d)
	if v!=0 and x!=0:
		if v==w: v=w=1
		elif v==x: v=x=1
		elif u==w: u=w=1
		elif u==x: u=x=1
		else: return False
		m = u*v/gcd(u*v,w*x)
		o = w*x/gcd(u*v,w*x)
		return  _n==m and _d==o
	return False
r,s=1,1
for n in xrange(11,100):
	for d in xrange(n+1,100):
		if reduce(n,d): r,s = r*n, s*d

print s/gcd(r,s)
