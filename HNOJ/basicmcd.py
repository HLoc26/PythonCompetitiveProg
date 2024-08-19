'''https://hnoj.edu.vn/problem/basicmcd'''
n, q = map(int, input().split())

arr = list(map(int, input().split()))

prefixSum = [0] * (len(arr) + 1)

for i in range(1, len(arr) + 1):
    prefixSum[i] += prefixSum[i-1] + arr[i-1]
# sum(l, r) = prefix[r+1] - prefix[l] 
# 1-indexed --> sum(l-1)
res = []
for _ in range(q):
    l, r = map(int, input().split())
    res.append(prefixSum[r] - prefixSum[l-1])

print('\n'.join(map(str, res)))