from collections import defaultdict
import sys

u, v = map(int, input().split())
lines = defaultdict(list)

for _ in range(v):
    start, end = map(int, sys.stdin.readline().split())
    lines[start] += [end]
    lines[end] += [start]
    

visited = [0] * (u)

count = 0
while sum(visited) != u:
    
    count += 1
    visit = lines[visited.index(0) + 1].copy()
    visited[visited.index(0)] = 1
    
    while visit:
        v = visit.pop()
        if not visited[v - 1]:
            visited[v - 1] = 1
            visit += lines[v]

print(count)