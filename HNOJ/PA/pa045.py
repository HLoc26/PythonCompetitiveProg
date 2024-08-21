'''https://hnoj.edu.vn/problem/pa045'''
n = int(input())

i = 2
while i*i <= n:
    if n % i:
        i+=1
    else:
        print(i, end=' ')
        n//=i
if n > 1:
    print(n)