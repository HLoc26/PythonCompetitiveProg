'''https://hnoj.edu.vn/problem/pa031'''
m = int(input())
n = int(input())
k = int(input())

s = str(m*n*k)

if len(s) < 2 or s[-1] != "0":
    print("NO")
else:
    print("YES")