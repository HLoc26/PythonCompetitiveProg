'''https://oj.vnoi.info/problem/lis'''
n = int(input())
a = list(map(int, input().split()))

# Binary search from index 0 to index high (not from 0 to last element)
def binarySearch(array, target, high):
    low = 0
    while low < high:
        mid = low + (high - low)//2
        if array[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def solve():
    if not a:
        return 0
    # Array that store the last element of the increasing subsequence that have length i
    tails = [0] * (n)
    size = 0 # Longest subsequence size

    for x in a:
        # Find the index where we put/replace x into the tail array,
        # make sure that tail is sorted all the way
        i = binarySearch(tails, x, size)
        tails[i] = x # Replace tails[i] by x, with every replacement, tails[i] becomes smaller
        # print(f"tails[{i}]: {tails[i]}") # Uncomment this to see better
        if i == size: # If i == size, that means x is the largest in tails,
            # print("i == size")
            size += 1 # means we found a longer subsequence
    # print(tails) 
    return size

print(solve())