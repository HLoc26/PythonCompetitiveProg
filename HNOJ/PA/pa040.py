'''https://hnoj.edu.vn/problem/pa040'''

# Factorize to count divisors, better for large n
def countDiv_factorize(n):
    factors = {}
    i = 2
    while i*i <= n:
        if n % i != 0:
            i+=1
        else:
            n//=i
            factors[i] = factors.get(i, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    res = 1

    for value in factors.values():
        res*=value+1
    return res

# Count divisors using loop
def countDiv_loop(n):
    count = 0
    for i in range(1, n//2+1):
        if n%i == 0:
            count+=1
            # print(i, n//i)
    return count+1

n = int(input())
print(countDiv_loop(n))
