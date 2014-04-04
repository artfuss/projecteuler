#! /usr/bin/env python

p = range(0, 40)
r = [i for i in xrange(40)]


def find(x):
    if x != p[x]:
        p[x] = find(p[x])
        return p[x]


def union(x, y):
    _x = find(x)
    _y = find(y)
    if r[_x] > r[_y]:
        p[_y] = _x
    else:
        p[_x] = _y
        if r[_x] == r[_y]:
            r[_y] += 1


import sys
import heapq

MAX, TOTAL = 0, 0
h = []
for i, l in enumerate(sys.stdin.readlines()):
    for j, e in enumerate(l.strip().split(',')):
        if e != '-':
            heapq.heappush(h, (int(e), i, j))
            TOTAL += int(e)
while h:
    e, i, j = heapq.heappop(h)
    if find(i) != find(j):
        MAX += e
        union(i, j)

print TOTAL / 2 - MAX
