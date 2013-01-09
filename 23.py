#! /usr/bin/env python
import math
def non_abundant(n):
  s = 1
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i == 0: 
			s += i
			if i != n/i: s+= n/i
	return s <= n
l=[-1]*28124
l[12]=1
for i in xrange(1,28124):
	
	if l[i] == 1:
		for j in xrange(2*i,28124,i):
			l[i]=1
	else:
		if i < 12 : l[i] = 0
		else:
			if non_abundant(i): 
				l[i] = 0 
			else: l[i] = 1
s = reduce(lambda x,y:x+y, range(1,24))
for i in xrange(24,28124):
	f = True
	for j in xrange(12,i/2+1):
		if l[j]==1 and l[i-j]==1:
			f = False
			break
	if f == True: 
		s += i
print s
