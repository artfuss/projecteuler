def expmod(a,b,p):
    res = 1
    while b > 0:
        if b%2==1:
            res = (res*a)%p
        b /= 2
        a = (a*a)%p
    return res
sum = 0
for i in xrange(1,1000):
    sum = (sum + expmod(i,i,10**10)) % 10**10
print sum
