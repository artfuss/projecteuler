#! /usr/bin/env python
import math
def solve(l):
  m=[[0 for i in xrange(len(l))] for j in xrange(len(l))]
	m[0][0]=l[0][0]
	for i in xrange(1,len(l)):
		for j in xrange(len(l[i])):
			if j==i:
				m[i][j] = l[i][j] + m[i-1][j-1]
			else:
				m[i][j] = l[i][j] + max(m[i-1][j],m[i-1][j-1])
	print max(m[len(l)-1])
import sys
l=[]
for i in sys.stdin.readlines():
	l.append(map(int,i.split()))
solve(l)
