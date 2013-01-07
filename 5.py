#! /usr/bin/python

def gcd(a,b):
  if b==0: return a
	else: return gcd(b,a%b)


def lcm(a,b):
	return a*b/gcd(a,b)

def solve():
	l=1
	for i in xrange(1,20,2):
		l = lcm(l, lcm(i,i+1))
	return l


'''
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("solve()", setup="from __main__ import solve"))

    '''
print solve()
