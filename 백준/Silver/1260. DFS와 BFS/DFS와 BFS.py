from collections import defaultdict, deque

N, M, V = map(int, input().split())

input_nums = []
for _ in range(M):
    input_nums.append(list(map(int, input().split())))
    
input_nums.sort()

bfs_visited = []
dfs_visited = []

points = defaultdict(list)
visit = deque()

for v1, v2 in input_nums:
    points[v1] += [v2]
    points[v2] += [v1]

visit += sorted(points[V], reverse=True)
dfs_visited.append(V)
while visit:
    v = visit.pop()
    if v not in dfs_visited:
        dfs_visited.append(v)
        visit += sorted(points[v], reverse=True)


visit += sorted(points[V])
bfs_visited.append(V)
while visit:
    v = visit.popleft()
    if v not in bfs_visited:
        bfs_visited.append(v)
        visit += sorted(points[v])


print(*dfs_visited)
print(*bfs_visited)