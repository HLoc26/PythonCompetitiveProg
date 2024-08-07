'''https://hnoj.edu.vn/problem/hnoi2122c2_arn'''
import sys
sys.stdin = open('ARN.INP','r')
sys.stdout = open('ARN.OUT','w')
S = input().strip()
X = input().strip()
count = 0
i = 0

while i <= len(S) - len(X):
    if S[i:i+len(X)] == X:
        count += 1
        i += len(X)
    else:
        i += 1
print(count)
