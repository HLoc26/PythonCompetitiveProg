'''https://hnoj.edu.vn/problem/biendoixau'''

# Đọc input
S = input().strip()
m = int(input())
a = list(map(int, input().split()))

n = len(S)
diff = [0] * (n + 1)

# Xử lý từng lần đảo
for ai in a:
    left, right = ai - 1, n - ai
    diff[left] ^= 1
    diff[right + 1] ^= 1

# Tính prefix xor
prefix_xor = 0
flip = [0] * n
for i in range(n):
    prefix_xor ^= diff[i]
    flip[i] = prefix_xor

# Xây dựng chuỗi kết quả
result = [''] * n
for i in range(n):
    if flip[i]:
        result[n-1-i] = S[i]
    else:
        result[i] = S[i]

print(''.join(result))


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