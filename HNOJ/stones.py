'''https://hnoj.edu.vn/problem/stones'''
n = int(input())
arr = list(map(int, input().split()))

# Two pointer
# Time: O(n)
# Space: O(1)
l = 0
maxL = arr[l]
r = len(arr) - 1
maxR = arr[r]
water = 0
while l < r:
    if maxL <= maxR:
        l += 1
        if maxL - arr[l] > 0:
            water += maxL - arr[l]
        maxL = max(maxL, arr[l])
    else:
        r -= 1
        if maxR - arr[r] > 0:
            water += maxR - arr[r]
        maxR = max(maxR, arr[r])

print(water)