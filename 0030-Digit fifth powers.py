def digitfifth(n):
    s = 0
    while n>0:
        s += (n%10)**5
        n /= 10
    return s
from operator import add
print reduce(add,[i for i in xrange(2,6*(9**5)) if i==digitfifth(i)])