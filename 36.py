#! /usr/bin/env python

def palin(s):
  if s[-1:]=='0': return False
	a=s[len(s)/2:]
	b=s[:len(s)/2]
	if len(s)%2==1:return a[1:][::-1]==b
	else: return a[::-1]==b

sum=0
for i in range(1,1000000):
	if palin(str(i)) and palin(bin(i)[2:]):
		sum += i

print sum
