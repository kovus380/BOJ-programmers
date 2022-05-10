#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, M;
vector<int> N_nums;

int binary(int num) {
    int start = 0;
    int end = N - 1;
    int mid;
    while (end >= start) {
        mid = (start + end) / 2;
        if (N_nums[mid] == num)
            return 1;
        else if (N_nums[mid] > num)
            end = mid - 1;
        else if (N_nums[mid] < num)
            start = mid + 1;
    }
    return 0;
}

int main() {
    ios_base::sync_with_stdio(0);cin.tie(0); 
    int tmp, num;
    cin >> N;
    for(int i = 0 ; i < N ; i++) {
        cin >> tmp;
        N_nums.push_back(tmp);
    }
    sort(N_nums.begin(), N_nums.end());
    
    cin >> M;
    for(int i = 0 ; i < M ; i++) {
        cin >> num;
        cout << binary(num) << '\n';
    }
}