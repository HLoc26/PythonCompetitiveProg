'''https://hnoj.edu.vn/problem/pa088'''
def getFibo(n): # Tìm các số fibonacci < n
    F = [0, 1]
    while F[-1] < n:
        F.append(F[-1] + F[-2])
    return F

n = int(input())
temp = n
F = getFibo(n)
res = []
for num in reversed(F):
    if temp <= 0:
        break
    if num <= temp:
        res.append(num)
        temp -= num
# print(sum(res) == n, res)
print(" ".join(map(str, res)))


