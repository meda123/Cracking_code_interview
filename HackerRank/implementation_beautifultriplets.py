import sys

x = map(int,raw_input().strip().split(' '))
n = x[0]
d = x[1]
a = map(int,raw_input().strip().split(' '))

count = 0
for i in xrange(n):
    if a[i] + d in a and a[i] + 2 * d in a:
        count += 1
print count



"""
Raw input: 
7 3
1 2 4 5 7 8 10
>>> 3

"""