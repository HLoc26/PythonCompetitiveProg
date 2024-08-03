'''https://hnoj.edu.vn/problem/biendoixau'''
'''AC 2/25, TLE 23/25'''
def find_odd_occurrences(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1

    odd_occurrences = [num for num, count in count.items() if count & 1]
    
    return odd_occurrences
s = input().strip()
m = int(input())
a = list(map(int, input().split()))

n = len(s)
a = find_odd_occurrences(a)
s = list(s)
for i in a:
    s[i-1:n-i+1] = s[i-1:n-i+1][::-1]

print(''.join(s))