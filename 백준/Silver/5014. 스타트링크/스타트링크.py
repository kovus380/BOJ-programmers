from collections import deque

f, s, g, u, d = map(int, input().split())

cases = [u, -d]

visited = [0] * f
need_visited = deque([[s, 0]])

while need_visited:

    v, depth = need_visited.popleft()

    if v == g:
        print(depth)
        exit()


    for case in cases:

        next = v + case
        if next < 1 or next > f or visited[next - 1]:
            continue

        visited[next - 1] = 1
        need_visited.append([next, depth + 1])

print("use the stairs")