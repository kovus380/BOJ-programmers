from collections import deque

N, K = map(int, input().split())

visit = deque([[0, N]])
visited = [0] * 1000001

while visit:
    depth, value = visit.popleft()
    if value < 0 or value > 1000000:
        continue
    if (value == K):
        print(depth)
        break
    if not visited[value]:
        visited[value] = 1
        visit += [[depth + 1, value - 1], [depth + 1, value + 1], [depth + 1, value * 2]]