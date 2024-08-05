'''https://hnoj.edu.vn/problem/pa027'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a <= d <= b or c <= b <= d:
    print("YES")
else:
    print("NO")