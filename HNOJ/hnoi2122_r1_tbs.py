'''https://hnoj.edu.vn/problem/hnoi2122_r1_tbs'''
import sys
sys.stdin = open('TBS.INP','r')
sys.stdout = open('TBS.OUT','w')
inp = []
for _ in range(4):
    inp.append(float(input()))

def check(inp):
    am = 0
    for num in inp:
        if num == 0:
            return 0
        if num < 0:
            am+=1
    if am & 1:
        return -1
    else:
        return 1
print(check(inp))