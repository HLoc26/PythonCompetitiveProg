'''https://hnoj.edu.vn/problem/pa050'''
a, n = map(int, input().split())

# print(pow(a, n))
# res = 1
# for _ in range(n):
#     res*= a
# print(res)

# Binary exponential
def binary_exp(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res*=a
        a*=a
        b//=2
    return res

print(binary_exp(a, n))