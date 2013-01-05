#! /usr/bin/env python

epoch = (1,1,1900)

def is_leap(y):
  if y%400==0:return True
	if y%4==0 and y%100!=0:return True
	return False
def days_in_a_month(m,y):
	if m==2:
		return 29 if is_leap(y) else 28 
	if m==4 or m==6 or m==9 or m==11:
		return 30
	return 31
def days_in_a_year(m1,m2,y):
	d = 0
	for m in xrange(m1,m2+1): d += days_in_a_month(m,y)
	return d 

def days_from_epoch(d,m,y):
	t = d + days_in_a_year(1,m-1,y)
	for Y in xrange(1900,y):
		t += days_in_a_year(1,13,Y)
	return t-1

s=0
for y in range(1901,2001):
	for m in range(1,13):
		if days_from_epoch(2,m,y)%7==0: s += 1
print s	





