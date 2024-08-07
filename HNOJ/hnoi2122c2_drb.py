'''https://hnoj.edu.vn/problem/hnoi2122c2_drb'''
import sys
sys.stdin = open('DRB.INP','r')
sys.stdout = open('DRB.OUT','w')

S1 = int(input())
V1 = int(input())
S2 = int(input())
V2 = int(input())

if S1 < S2 and V1 <= V2:
    time = -1
elif S1 > S2 and V1 >= V2:
    time = -1
else:
    time = abs(S2-S1) / abs(V2-V1)

print(int(time))
