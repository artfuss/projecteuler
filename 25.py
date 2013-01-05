#! /usr/bin/python

a,b,i,c=1,1,3,0

while c/10**999 == 0:
  c=a+b
  a,b,i=b,c,i+1

print i-1
