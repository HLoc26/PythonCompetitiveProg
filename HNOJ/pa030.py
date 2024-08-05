'''https://hnoj.edu.vn/problem/pa030'''
a = int(input())
b = int(input())
c = int(input())

a, b, c = sorted([a, b, c])

if c / b == b / a:
    print("YES")
else:
    print("NO")
    
