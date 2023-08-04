from collections import defaultdict, deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

family = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    family[x] += [y]
    family[y] += [x]

visited = [0] * n
need_visit = deque([[n, 1] for n in family[a]])

while need_visit:

    v, depth = need_visit.popleft()

    visited[v - 1] = 1

    if v == b:
        print(depth)
        exit()

    
    need_visit += deque([[n, depth + 1] for n in family[v] if not visited[n - 1]])
    
print(-1)