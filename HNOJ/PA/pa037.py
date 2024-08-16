'''https://hnoj.edu.vn/problem/pa037'''
n = int(input())

interest = 0.07

for i in range(10):
    n += int(n*interest)
    print(n)