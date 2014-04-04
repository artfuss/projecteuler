#! /usr/bin/env python
from math import sqrt


def d(a):
    res = 1
    for i in xrange(2, int(sqrt(a))):
        j = 1
        while a % i == 0:
            j += 1
            a /= i
        res *= (i ** j - 1) / (i - 1)
    if a > 1:
        res *= a + 1
    return res


if __name__ == '__main__':
    res = 0
    for a in xrange(2, 10000):
        b = d(a) - a
        if a != b and b < 10000 and a == d(b) - b:
            res += a + b

    print res >> 1
