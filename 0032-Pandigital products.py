def pandigital(a,b):
    return ''.join(sorted(str(a)+str(b)+str(a*b))) == '123456789'
sum = 0
seen = {}
for i in xrange(1,99):
    for j in xrange(100,9999):
        if pandigital(i,j) and i*j not in seen:
            seen[i*j] = True
            print i,'X',j,'=',i*j
            sum += i*j

print sum