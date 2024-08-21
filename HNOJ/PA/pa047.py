'''https://hnoj.edu.vn/problem/pa047'''

def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
    return [str(num) for num in range(2, n+1) if primes[num]]

n = int(input())
print('\n'.join(sieve(n)))