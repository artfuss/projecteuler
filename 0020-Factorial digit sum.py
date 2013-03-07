#! /usr/bin/env python
import operator
def factorial():
	return reduce(operator.mul,range(1,101))

n = factorial()
s = 0
while n:
	s += n%10
	n /= 10
print s