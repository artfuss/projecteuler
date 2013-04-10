fact = [1]*10
for i in xrange(1,10):
    fact[i] = i*fact[i-1]
def factorian(n):
    s = 0
    while n > 0:
        s += fact[n%10]
        n /= 10
    return s

from operator import add
print reduce(add,[i for i in xrange(3,7*fact[9],2) if i==factorian(i)])