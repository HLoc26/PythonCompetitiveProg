'''https://hnoj.edu.vn/problem/pa093'''
import sys
sys.stdin = open('3SEQ.INP','r')
sys.stdout = open('3SEQ.OUT','w')
# Đọc số n
n = int(input())

# Đọc ba dãy số A, B, C
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Tính tổng lớn nhất
max_sum = 0
for i in range(n):
    column_sum = A[i] + B[i] + C[i]
    max_sum = max(max_sum, column_sum)

# In kết quả
print(max_sum)