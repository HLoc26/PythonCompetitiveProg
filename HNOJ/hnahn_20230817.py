'''https://hnoj.edu.vn/problem/hnahn_20230817'''
'''AC 5/10, TLE 5/10'''
def find_min_b(a):
    low, high = 1, B // a
    while low <= high:
        mid = (low + high) // 2
        if a * mid >= A:
            high = mid - 1
        else:
            low = mid + 1
    return low

def find_max_b(a):
    low, high = 1, B // a
    while low <= high:
        mid = (low + high) // 2
        if a * mid <= B:
            low = mid + 1
        else:
            high = mid - 1
    return high
A, B, C, D = map(int, input().split())
count = 0
for a in range(1, int(B**0.5) + 1):
    min_b = find_min_b(a)
    max_b = find_max_b(a)
    if min_b > max_b:
        continue
    for b in range(max_b, min_b - 1, -1):
            if a > b:
                break
            s = a * b
            p = 2 * (a + b)
            if A <= s <= B and C <= p <= D:
                count += 1

print(count)