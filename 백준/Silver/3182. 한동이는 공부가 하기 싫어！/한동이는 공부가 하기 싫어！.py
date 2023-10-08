from collections import deque


n = int(input())
nexts = [int(input()) for _ in range(n)]

answer = 0
max_ask_cnt = 0

for i in range(1, n + 1):
    visited = [0] * n
    next_visit = deque([i])

    ask_cnt = 0

    while next_visit:
        
        v = next_visit.popleft()
        
        if visited[v - 1] == 1:
            break

        visited[v - 1] = 1
        ask_cnt += 1
        next_visit.append(nexts[v - 1])

    if ask_cnt > max_ask_cnt:
        answer = i
        max_ask_cnt = ask_cnt

print(answer)