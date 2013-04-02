#! /usr/bin/env python
p = 0
s = 1
for k in xrange(2,7):
    p += 9*(k-1)*(10**(k-2))
    i = 10**k - p
    t = 10**(k-1) + i/k + 1
    r = 10**(k - i%k)
    s *= (t/r)%10
        
print s
