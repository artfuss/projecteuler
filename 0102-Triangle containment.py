#! /usr/bin/env python

import sys
def solve(p):
  a = p[0]*p[3]-p[1]*p[2]
	b = p[2]*p[5]-p[3]*p[4]
	c = p[4]*p[1]-p[5]*p[0]
	if a>0 and b>0 and c>0:return True
	if a<0 and b<0 and c<0:return True
	return False
sum = 0
for l in sys.stdin.readlines():
	if(solve(map(int,l.strip().split(',')))): sum += 1
print sum
