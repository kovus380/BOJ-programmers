import sys


n, m, k, x = map(int, input().split())


graph = dict()
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a in graph:
        graph[a] += [b]
    else:
        graph[a] = [b]


depth = 0
depth_visited = []
haveto_visit = [x]

answer = []

while depth <= k:

    while haveto_visit:
        tmp = haveto_visit.pop()

        if not visited[tmp]:
            if depth == k:
                answer.append(tmp)
            if tmp in graph:
                depth_visited += graph[tmp]
            
        visited[tmp] = 1
        
    depth += 1
    haveto_visit = depth_visited
    depth_visited = []

answer.sort()

if answer:
    for a in answer:
        print(a)
else:
    print(-1)