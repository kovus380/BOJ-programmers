from collections import deque


N = int(input())

visit = deque([[0, N]])
visited = []

answer = 0

while visit:
    
    v = visit.popleft()

    if v[1] == 1:
        answer = v[0]
        break

    if v[1] not in visited:
        visited.append(v[1])
        if (v[1] % 3 == 0):
            visit.append([v[0] + 1, v[1] // 3])
        if (v[1] % 2 == 0):
            visit.append([v[0] + 1, v[1] // 2])
        visit.append([v[0] + 1, v[1] - 1])

print(answer)