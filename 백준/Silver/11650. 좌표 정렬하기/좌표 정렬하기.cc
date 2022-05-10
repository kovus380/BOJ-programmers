#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
    int N, tmp1, tmp2;
    vector<pair<int, int>> nums;
    
    cin >> N;
    
    for(int i = 0 ; i < N ; i++) {
        cin >> tmp1 >> tmp2;
        nums.push_back({tmp1, tmp2});
    }
    
    sort(nums.begin(), nums.end());
    
    for(int j = 0 ; j < N ; j++) {
        cout << nums[j].first << ' ' << nums[j].second << '\n';
    }
}