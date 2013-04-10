def main():
    N = (10**7)/2
    primes = [1]*N

    i = 1
    while i*i <= N:
        for j in xrange(2*i*(i+1),N,2*i+1): primes[j]=0
        i += 1

    from itertools import permutations
    for i in permutations(range(7,0,-1)):
        y = 0
        for x in i: y = 10*y + x
        if y % 2 !=0 and  primes[(y-1)/2]==1:
            print y
            return

main()