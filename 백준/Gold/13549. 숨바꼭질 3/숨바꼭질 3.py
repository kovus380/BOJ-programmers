from collections import deque

n, k = map(int, input().split())

bfs = deque([[n, 0]])

visit = [0] * 200001

answer = []

while bfs:

    location, time = bfs.popleft()

    if location == k:
        answer.append(time)
        continue

    if location < 0 or location > 150000 or visit[location] == 1 :
        continue

    else:
        visit[location] = 1

    bfs.appendleft([location * 2, time])
    bfs.extend([[location + 1, time + 1], [location - 1, time + 1]])

print(min(answer))