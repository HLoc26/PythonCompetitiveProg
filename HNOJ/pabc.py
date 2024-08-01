'''https://hnoj.edu.vn/problem/pabc'''
n = int(input())

count = 0
a = 1
while a < n**(1/3) + 1:
    b = a
    p2 = n//a
    while b < p2**(0.5) + 1:
        c = p2 // b
        if a * b * c == n:
            print(a, b, c)
            count+=1
        b+=1
    a+=1
    
print(count)
