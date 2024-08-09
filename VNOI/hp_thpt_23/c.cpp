#include <cmath>
#include <iostream>

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
        }
        else {
            cout << 0 << '\n';
        }
    }

    return 0;
}
