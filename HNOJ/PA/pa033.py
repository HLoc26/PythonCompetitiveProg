'''https://hnoj.edu.vn/problem/pa033'''

x = int(input())
y = int(input())

thang31 = [1, 3, 5, 7, 8, 10, 12]
thang30 = [4, 6, 9, 11]

leap = (y % 4 == 0 and y % 100) or y % 400 == 0
if x in thang31:
    print(31)
elif x in thang30:
    print(30)
else:
    if leap:
        print(29)
    else:
        print(28)
