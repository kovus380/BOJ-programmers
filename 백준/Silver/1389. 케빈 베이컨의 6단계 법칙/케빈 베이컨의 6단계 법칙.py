from collections import defaultdict, deque
import sys

connect = defaultdict(list)

N, M = map(int, input().split())

for _ in range(M):
    start, end = map(int, input().split())
    connect[start] += [[end, 0]]
    connect[end] += [[start, 0]]

an = [5001, 0]

for i in range(1, N + 1):
    answer = [0] * (N + 1)
    answer[i] = 1
    visit = deque()
    visit += connect[i]
    visited = [i]
    while visit:
        v, depth = visit.popleft()
        if not answer[v]:
            answer[v] = depth + 1
            for k in connect[v]:
                visit.append([k[0], depth + 1])
    temp = sum(answer) - 1
    if temp < an[0]:
        an = [temp, i]

print(an[1])