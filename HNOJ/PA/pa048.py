'''https://hnoj.edu.vn/problem/pa048'''
def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

def LCM(a, b):
    return int((a*b) / GCD(a, b))

a = int(input())
b = int(input())
print(GCD(a, b))
print(LCM(a, b))