from collections import defaultdict, deque
import sys


N = int(input())

graph = defaultdict(list)

for i in range(N):
    for idx, j in enumerate(input().split()):
        if j == '1':
            graph[i] += [idx]


for i in range(N):
    answer = ["0"] * N
    
    visit = deque(graph[i])
    
    while visit:
        v = visit.popleft()
        if answer[v] == "0":
            answer[v] = "1"
            visit += graph[v]
    print(' '.join(answer))
        


