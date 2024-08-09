#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

bool has_pair(const vector<int> &arr, int k) {
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
        }
        else {
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
        }
        else {
            results += '0';
        }
    }

    cout << results << endl;
    return 0;
}
