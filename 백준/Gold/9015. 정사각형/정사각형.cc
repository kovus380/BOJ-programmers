#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2,fma")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
 
#include "bits/stdc++.h"
#include "ext/rope"
 
using namespace std;
using namespace __gnu_cxx;
 
using ll = long long;
using pii = pair<int, int>;
 
template<typename T>
struct point2 {
  T x, y;
  point2() : x(0), y(0) {}
  point2(T _x, T _y) : x(_x), y(_y) {}
 
  bool operator < (const point2<T> &r) const {
    if (typeid(T) == typeid(int)) {
      if (x != r.x) return x < r.x;
      return y < r.y;
    } else {
      if (fabs(x - r.x) >= 1e-9) return x < r.x;
      return y < r.y;
    }
  }
 
  bool operator == (const point2<T> &r) const {
    if (typeid(T) == typeid(int)) {
      return x == r.x and y == r.y;
    } else {
      return (fabs(r.x - x) < 1e-9 and fabs(r.y - y) < 1e-9);
    }
  }
};
 
inline int dist_sq(point2<int> &l, point2<int> &r) {
  return (r.x - l.x) * (r.x - l.x) + (r.y - l.y) * (r.y - l.y);
}
 
int n;
point2<int> ar[3000];
set<point2<int>> st;
 
void solve()
{
  st.clear();
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> ar[i].x >> ar[i].y;
    st.insert(ar[i]);
  }
  sort(ar, ar + n);
 
  int ans = 0;
 
  for (int i = 0; i < n; i++)
  {
    for (int j = i + 1; j < n; j++)
    {
      int dx = ar[j].x - ar[i].x;
      int dy = ar[j].y - ar[i].y;
      point2<int> tmp = ar[i];
      tmp.x -= dy;
      tmp.y += dx;
      if (!st.count(tmp)) continue;
 
      tmp = ar[j];
      tmp.x -= dy;
      tmp.y += dx;
      if (!st.count(tmp)) continue;
 
      ans = max(ans, dx * dx + dy * dy);
    }
  }
 
  cout << ans << '\n';
}
 
int main()
{
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
//  freopen("output.txt", "w", stdout);
#endif
  cin.tie(nullptr);
  ios::sync_with_stdio(false);
 
  int t;
  cin >> t;
  while (t--)
  {
    solve();
  }
}
