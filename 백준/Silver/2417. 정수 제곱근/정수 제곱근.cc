#include <iostream>
#include<cmath>
using namespace std;
int main() {
    long long n;
    long long i = 0;
    
    cin >> n;
    i = sqrt(n);
    
    if(n > (i * i))
        i++;
    cout << i;
    return 0;
}