'''https://hnoj.edu.vn/problem/pa012'''

def sumDigitStr(n):
    return sum(int(char) for char in str(n))

def sumDigitArithmetic(n):
    total = 0
    while n != 0:
        total += n % 10
        n//=10
    return total

n = int(input())
print(sumDigitStr(n))
print(sumDigitArithmetic(n))