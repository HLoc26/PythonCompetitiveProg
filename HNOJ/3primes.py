'''https://hnoj.edu.vn/problem/3primes'''
def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
    return [i for i in range(2, n+1) if primes[i]]

n = int(input())
limit = 10**6 + 1
primes = sieve(limit)
max_k = 0
for i in range(0, len(primes) - 2):
    k = primes[i] * primes[i+1] * primes[i+2]
    if max_k < k <= n:
        max_k = k

print(max_k)

