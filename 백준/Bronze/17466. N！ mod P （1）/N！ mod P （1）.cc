#include <iostream>
using namespace std;
int main(){
    unsigned long long n, p;
    cin >> n >> p ;
    unsigned long long res = 1;
    for (unsigned long long i = 1 ; i <= n ; i++){
      res = res * i;
      res = res % p;
    }
    cout << res;
}