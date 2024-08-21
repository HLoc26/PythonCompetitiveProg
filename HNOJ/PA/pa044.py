'''https://hnoj.edu.vn/problem/pa044'''

n = int(input())

i = 0
f1 = 0
f2 = 1
while i < n:
    t = f2
    f2 = f1 + f2
    f1 = t
    i+=1

print(f1)