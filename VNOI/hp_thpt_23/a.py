'''https://oj.vnoi.info/problem/hp_thpt_23_a'''
def factor(n):
    f = {}
    i = 2
    while i*i <= n:
        if n % i:
            i+=1
        else:
            n//=i
            f[i] = f.get(i, 0) + 1
    if n > 0:
        f[n] = f.get(n, 0) + 1
    return list(f.values())

n = int(input())

if n < 2:
    print(1)
else:

    f = factor(n)
    res = 1
    for i in range(len(f)):
        res *= f[i] + 1
    print(res)