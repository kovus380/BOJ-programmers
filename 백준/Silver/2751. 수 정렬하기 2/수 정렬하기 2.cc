#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
    int N, tmp;
    vector<int> nums;
    
    cin >> N;
    
    for(int i = 0 ; i < N ; i++) {
        cin >> tmp;
        nums.push_back(tmp);
    }
    
    sort(nums.begin(), nums.end());
    for(int j = 0 ; j < N ; j++) {
        cout << nums[j] << '\n';
    }
}