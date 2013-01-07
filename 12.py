#! /usr/bin/python

import math 
from  itertools import *
N = 10000000000
l = [1 for i in xrange(N)]
for i in xrange(2,N):
  if l[i] == 1:
		j = 2*i
		while j < N:
			l[j]=0
			j += i

def divisors(n):
	sum = 1
	for i in xrange(2,int(math.sqrt(n))+1):
		if l[i]==1:
			x=0
			while n!=0 and n%i==0:
				x += 1
				n /= i
			sum *= (x+1)
	if n>1:
		sum *= 2
	return sum

i=10000000000
while divisors(i) != 501:
	i += 1
print i
