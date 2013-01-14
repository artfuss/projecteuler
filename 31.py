#! /usr/bin/env python
target = 200
ways=[0]*(target+1)
ways[0] = 1
coins = [1,2,5,10,20,50,100,200]
for j in coins:
  for i in xrange(j,201):
		ways[i] += ways[i-j]
print ways[200]
