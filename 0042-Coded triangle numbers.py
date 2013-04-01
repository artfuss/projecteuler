from math import sqrt
from urllib2 import urlopen
from operator import add
def is_triangle(n):
    t = int(sqrt(2*n))
    if t*(t+1)==2*n: return True
    return False
def main():
    f = urlopen('http://projecteuler.net/project/words.txt')
    sum = 0
    for word in f.readline().split(','):
        ordw = reduce(add, map(lambda x: ord(x)-ord("A")+1, list(word.strip('"'))))
        if is_triangle(ordw): sum += 1
    print sum
if __name__ == '__main__':
    main()
