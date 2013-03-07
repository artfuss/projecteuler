#! /usr/bin/env python
import sys
l = [i.strip('"') for i in sys.stdin.readline().split(',')]
l.sort()

sum = 0
for i,w in enumerate(l):
  a=0
	for c in w:
		a = a + ord(c) - ord('A') + 1
	sum = sum + (i+1)*a
print sum
