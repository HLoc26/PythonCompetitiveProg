'''https://hnoj.edu.vn/problem/pa039'''
n = int(input())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def factorial_loop(n):
    res = 1
    for i in range(1, n+1):
        res*=i
    return res

e = 1
for i in range(1, n+1):
    e += 1/factorial(i)

print(e)