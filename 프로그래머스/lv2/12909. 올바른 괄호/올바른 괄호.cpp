#include<string>
#include <iostream>
#include <stack>
#include <cstring>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int cnt = 0;
    stack<char> st;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') {
            st.push('(');
        } else {
            if (st.empty()) {
                return false;
            } else {
                st.pop();
            }
        }
    }
    if (!st.empty()) {
        return false;
    }
    return true;
}