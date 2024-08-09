'''https://oj.vnoi.info/problem/tht21_kvb_seq'''
# prefix sum
def prefixS(arr):
    prefix = [0] * (len(arr)+1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
    return prefix

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
prefix = prefixS(arr)
print(prefix)

# print(prefix[2+1] - prefix[0]) # sum(i, j) = prefix[j+1] - prefix[i]
maxSum = float('-inf')
first_occurance = {}
for i, ai in enumerate(arr):
    if ai not in first_occurance:
        first_occurance[ai] = i

    currSum = prefix[i+1] - prefix[first_occurance[ai]]
    maxSum = max(maxSum, currSum)

print(maxSum)
