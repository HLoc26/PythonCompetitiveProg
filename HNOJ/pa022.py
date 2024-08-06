'''https://hnoj.edu.vn/problem/pa022'''
a = float(input())
b = float(input())
c = float(input())

a, b, c = sorted([a,b,c])

if c**2 == a**2 + b**2:
    print("VUONG")
elif a < b + c and b < a + c and c < a + b:
    print("CO")
else:
    print("KHONG")