'''https://hnoj.edu.vn/problem/pa052'''
n = int(input())
res = ''
while n > 0:
    res = str(n % 2) + res
    n//=2
print(res)