'''https://hnoj.edu.vn/problem/divide3'''
import sys
sys.stdin = open('DIV3.INP','r')
sys.stdout = open('DIV3.OUT','w')

a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
min_len = (b - a) / 3
if min_len != int(min_len):
    print(-1)
else:
    print(int(a + min_len), int(a + 2*min_len))