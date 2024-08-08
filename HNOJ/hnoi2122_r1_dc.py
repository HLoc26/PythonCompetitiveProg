'''https://hnoj.edu.vn/problem/hnoi2122_r1_dc'''
# AC 8/10, WA 2/10
import sys
sys.stdin = open('DC.INP','r')
sys.stdout = open('DC.OUT','w')

n, k = map(int, input().split())
d = {}
for _ in range(n):
    a, b = map(int, input().split())
    d[a] = d.get(a, 0) + 1
    d[b+1] = d.get(b+1, 0) - 1
points = sorted(d.keys())
curr = 0
ans = 0
# Check if d[i] == k
for i in range(len(points) - 1):
    curr += d[points[i]]
    if curr == k:
        ans += points[i+1] - points[i]


print(ans)
