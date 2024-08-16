'''https://hnoj.edu.vn/problem/pa035'''
a = int(input())
b = int(input())
c = int(input())


if max(a, b, c)**2 == (sum([a, b, c]) - (min(a,b,c) + max(a, b, c)))**2 + min(a, b, c)**2:
    print("Vuong")
elif a == b == c:
    print("Deu")
elif a == b or a == c or b == c:
    print("Can")
else:
    print("Thuong")