import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())

dict = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    dict[a] += [b]
    dict[b] += [a]

need_visit = deque([1])
parents = [0] + [0] + [0] * (n - 1)

while need_visit:
    node = need_visit.popleft()

    if node in dict:
        for n in dict[node]:
            if parents[n]:
                continue
            need_visit.append(n)
            parents[n] = node


for parent in parents[2:]:
    print(parent)