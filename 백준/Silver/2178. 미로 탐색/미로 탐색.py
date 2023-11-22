from collections import deque
n, m = map(int, input().split())

grids = []
for _ in range(n):
    grids.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

next_visited = deque([[grids, 1, [0, 0]]])

answer = 100001

visited = [[0] * m for _ in range(n)]

# def pnext_visit(next_visited):
#     for i in range(len(next_visited)):
#         print(next_visited[i])

while next_visited:
    v_grid, v_cnt, v_next = next_visited.popleft()
    v_grid[v_next[0]][v_next[1]] = "0"
    if visited[v_next[0]][v_next[1]] >= v_cnt:
        continue 
    visited[v_next[0]][v_next[1]] = v_cnt
    # print(v_cnt)
    # pnext_visit(next_visited)

    if v_grid[n-1][m-1] == "0":
        answer = min(v_cnt, answer)
        # print("len", len(next_visited))
        continue

    for i in range(4):
        grid_temp = v_grid
        # grid_temp[v_next[0]][v_next[1]] = "0"
        if v_next[0] + dx[i] in range(n) and \
            v_next[1] + dy[i] in range(m) and \
                grid_temp[v_next[0] + dx[i]][v_next[1] + dy[i]] == "1":
            
            # pnext_visit(grid_temp)
            next_visited.append([grid_temp, v_cnt + 1, [v_next[0] + dx[i], v_next[1] + dy[i]]])

print(answer)