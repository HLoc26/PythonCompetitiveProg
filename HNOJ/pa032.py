'''https://hnoj.edu.vn/problem/pa032'''
n = int(input())

nhuan = (n % 4 == 0 and n % 100) or n % 400 == 0
print(366 if nhuan else 365)