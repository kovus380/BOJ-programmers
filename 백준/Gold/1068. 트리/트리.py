from collections import defaultdict, deque

n = int(input())
parents = list(map(int, input().split()))
rem_node = int(input())

root = 0
nodes = defaultdict(list)

for idx, parent in enumerate(parents):
    if parent == -1:
        root = idx
        continue
    nodes[parent] += [idx]

need_visited = deque([rem_node])

while need_visited:
    v = need_visited.popleft()
    need_visited += nodes[v]
    nodes.pop(v)

answer = 0

need_visited = deque([[root]]  if nodes else [])
while need_visited:
    visited = need_visited.popleft()
    if visited[-1] not in nodes or nodes[visited[-1]] == [rem_node]:
        answer += 1
    else:
        need_visited += [ visited + [n] for n in nodes[visited[-1]] if not n == rem_node]

print(answer)