'''https://oj.vnoi.info/problem/hp_thpt_23_d'''

# Honestly, this problem set is not for Python. 
# This problem can be solved in 2 ways, the short way, and the longer way. 
# The longer way is in the comment, and it can AC if only the code is in C/C++
# In Python, the longer way can only AC 12/20

# Short
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = input()
    if k & 1:
        print(1, end='')
    else:
        print(0, end='')

''' Long
def has_pair(arr, k):
    evens = set()
    odds = set()
    
    for num in arr:
        if num > k:
            continue
        if num % 2 == 0:
            if k - num in odds:
                return True
            evens.add(num)
        else:
            if k - num in evens:
                return True
            odds.add(num)
    
    return False

# Đọc số lượng bộ test
t = int(input())

results = []

for _ in range(t):
    # Đọc N và k
    N, k = map(int, input().split())
    
    # Đọc dãy số
    arr = list(map(int, input().split()))
    
    # Kiểm tra và lưu kết quả
    if has_pair(arr, k):
        results.append('1')
    else:
        results.append('0')

# In kết quả
print(''.join(results))
'''

# Long but in C/C++
'''
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

bool has_pair(const vector<int>& arr, int k) {
    unordered_set<int> evens;
    unordered_set<int> odds;

    for (int num : arr) {
        if (num > k) {
            continue;
        }
        if (num % 2 == 0) {
            if (odds.find(k - num) != odds.end()) {
                return true;
            }
            evens.insert(num);
        } else {
            if (evens.find(k - num) != evens.end()) {
                return true;
            }
            odds.insert(num);
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    string results;

    while (t--) {
        int N, k;
        cin >> N >> k;

        vector<int> arr(N);
        for (int i = 0; i < N; ++i) {
            cin >> arr[i];
        }

        if (has_pair(arr, k)) {
            results += '1';
        } else {
            results += '0';
        }
    }

    cout << results << endl;
    return 0;
}
'''