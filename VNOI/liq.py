'''https://oj.vnoi.info/problem/liq'''
n = int(input())
a = list(map(int, input().split()))

right = float('inf')
left = float('-inf')
a.append(right)
a = [left] + a

L = [0] * (n+2)
L[n+1] = 1
T = [0] * (n+2)
res = []
for i in range(n, -1, -1):
    jmax = n+1
    for j in range(i+1, n+2):
        if a[j] > a[i] and L[j] > L[jmax]:
            jmax = j
    L[i] = L[jmax] + 1
    T[i] = jmax
print(L[0] - 2)

# # Traceback
# i = T[0]
# while i != n+1:
#     print(a[i], end=' ')
#     i = T[i]