#! /usr/bin/env python

g={}
g[0]=0
g[1]=len('one')
g[2]=len('two')
g[3]=len('three')
g[4]=len('four')
g[5]=len('five')
g[6]=len('six')
g[7]=len('seven')
g[8]=len('eight')
g[9]=len('nine')
g[10]=len('ten')
g[11]=len('eleven')
g[12]=len('twelve')
g[13]=len('thirteen')
g[14]=len('fourteen')
g[15]=len('fifteen')
g[16]=len('sixteen')
g[17]=len('seventeen')
g[18]=len('eighteen')
g[19]=len('nineteen')
g[20]=len('twenty')
g[30]=len('thirty')
g[40]=len('forty')
g[50]=len('fifty')
g[60]=len('sixty')
g[70]=len('seventy')
g[80]=len('eighty')
g[90]=len('ninety')
g[100]=len('hundred')
g[1000]=len('thousand')

def onedigit(n):
  return g[n]
def twodigits(n):
	if n not in g:
		return g[n-n%10]+onedigit(n%10)
	else:
		return g[n]
def threedigits(n):
	s = g[n/100]+g[100]
	t = twodigits(n%100)
	if t!=0:return s+3+t
	else:return s
	

sum = g[1]+g[1000]
for i in xrange(1,1001):
	if i>=1 and i<=9: sum += onedigit(i)
	if i>=10 and i<=99: sum += twodigits(i)
	if i>=100 and i<=999: sum += threedigits(i)
print sum
