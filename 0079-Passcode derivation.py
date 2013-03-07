#! /usr/bin/python
from collections import defaultdict
g = defaultdict(set)
for l in [l.strip() for l in open('./keylog.txt')]:
  g[l[0]].add(l[1])
	g[l[0]].add(l[2])
	g[l[1]].add(l[2])
vis = []
def dfs(s):
	for u in g[s]:
		if u not in vis:
			dfs(u)
	vis.append(s)

def dfs_a():
	for s in g.keys():
		if s not in vis:
			dfs(s)
dfs_a()
print ''.join(reversed(vis))
