def Find(arr):
    n = len(arr)
    if n <= 1:
        return n, arr
    
    start = 0
    maxLen = 1
    maxStart = 0
    currLen = 1
    
    for i in range(1, n):
        if (arr[i] > 0 and arr[i-1] < 0) or (arr[i] < 0 and arr[i-1] > 0):
            currLen += 1
            if currLen > maxLen:
                maxLen = currLen
                maxStart = start
        else:
            start = i
            currLen = 1
    
    return maxLen, arr[maxStart:maxStart+maxLen]

n = int(input())
arr = list(map(int, input().split()))

length, subarray = Find(arr)

print(f"{length}")
print(' '.join(map(str, subarray)))