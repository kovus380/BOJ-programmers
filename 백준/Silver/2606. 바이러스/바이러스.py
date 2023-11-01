from collections import defaultdict, deque

ver_cnt = int(input())
node_cnt = int(input())

graph = defaultdict(list)

for i in range(node_cnt):
    s, e = map(int, input().split())
    graph[s] += [e]
    graph[e] += [s]


visited = [0] * (ver_cnt + 1)

need_visited = deque([1])
visited[1] = 1

answer = 0

while need_visited:
    v = need_visited.popleft()

    answer += 1

    for next_visit in graph[v]:
        if visited[next_visit] == 0:
            need_visited.append(next_visit)
            visited[next_visit] = 1

print(answer - 1)