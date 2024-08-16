'''https://hnoj.edu.vn/problem/pa036'''

n = int(input())

i = 1
while n*2**i < 10**9:
    i+=1

print(10**9 // (n*2**19))

'''
from math import log2
n = int(input())

i = int(log2((10**9 - 1) / n)) + 1

print(i)
'''