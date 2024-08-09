'''https://oj.vnoi.info/problem/hp_thpt_23_c'''
# This problem can't be AC with Python since the language require more time than C/C++
# Though, I AC 14/20 with this solution
# Better solution would be sieve of eratosthenes
# C++ below
def prefixS(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
    return prefix

def isPrime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i+=6
    return True

n, m = map(int, input().split())
a = list(map(int, input().split()))
uv = []
for _ in range(m):
    uv.append(list(map(int, input().split())))
prefix = prefixS(a)
for i in range(len(uv)):
    u = uv[i][0] - 1
    v = uv[i][1] - 1
    s = prefix[v+1] - prefix[u]
    if isPrime(s):
        print(1)
    else:
        print(0)


'''
#include <iostream>
#include <cmath>

using namespace std;

// Function to compute the prefix sums
void computePrefixSums(const int arr[], long long prefix[], int n) {
    prefix[0] = 0;
    for (int i = 1; i <= n; ++i) {
        prefix[i] = prefix[i - 1] + arr[i - 1];
    }
}

// Function to check if a number is prime
bool isPrime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    int a[n];
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int queries[m][2];
    for (int i = 0; i < m; ++i) {
        cin >> queries[i][0] >> queries[i][1];
    }

    long long prefix[n + 1];
    computePrefixSums(a, prefix, n);

    for (int i = 0; i < m; ++i) {
        int u = queries[i][0] - 1;
        int v = queries[i][1] - 1;
        long long sum = prefix[v + 1] - prefix[u];
        if (isPrime(sum)) {
            cout << 1 << '\n';
        } else {
            cout << 0 << '\n';
        }
    }

    return 0;
}
'''