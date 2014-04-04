from math import sqrt

#
#   count of all divisors of a number
#


def num_of_divisors(n):
    if n == 1:
        return 1
    res = 1
    for i in xrange(2, int(sqrt(n))):
        j = 0
        while n % i == 0:
            j += 1
            n /= i
        res *= (j + 1)
    if n > 1:
        res *= 2
    return res


def main():
    """

    Module Entry point
    """
    prev, curr = num_of_divisors(1), 1
    for i in xrange(2, 10 ** 5):
        curr = num_of_divisors(i) if i % 2 else num_of_divisors(i / 2)
        if prev * curr > 500:
            print (i * (i - 1)) / 2
            break
        prev = curr


if __name__ == '__main__':
    main()
