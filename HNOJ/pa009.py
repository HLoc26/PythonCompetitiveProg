'''https://hnoj.edu.vn/problem/pa009'''
a = float(input())
b = float(input())
c = float(input())

p = (a+b+c)/2

s = (p*(p-a)*(p-b)*(p-c))**0.5

print(s)