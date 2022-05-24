#include <iostream>
using namespace std;
unsigned long long a, b, c, k;

unsigned long long power(unsigned long long b) {
	if (b == 0) return 1;
	if (b == 1) return a % c;
	
	k = power(b / 2) % c;
	if (b % 2 == 0) return k * k % c;
	return k * k % c * a % c;
}

int main() {
	cin >> a >> b >> c; 
	cout << power(b);
}
