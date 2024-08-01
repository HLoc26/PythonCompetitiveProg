'''https://hnoj.edu.vn/problem/pa012'''
# Same as pa012 but larger limit
def sumDigitArithmetic(n):
    total = 0
    while n != 0:
        total += n % 10
        n//=10
    return total

n = int(input())
print(sumDigitArithmetic(n))