'''https://hnoj.edu.vn/problem/pa019'''
a = int(input())
b = int(input())
c = int(input())

condition = (a < b + c and b < a + c and c < a + b) and (a > 0 and b > 0 and c > 0)

print("YES" if condition else "NO")