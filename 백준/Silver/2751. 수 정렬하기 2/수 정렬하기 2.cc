#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> v(N);
    for(int i = 0 ; i < N ; i++){
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    for(int j = 0 ; j < N ; j++){
        cout << v[j] << '\n';
    }
}