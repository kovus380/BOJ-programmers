import copy
from itertools import combinations

n, m = map(int, input().split())

grid = []
virus = []
zeros = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for nn in range(n):
    input_list = list(map(int, input().split()))
    grid.append(input_list)
    for mm in range(m):
        if grid[nn][mm] == 2:
          virus.append([nn, mm])  
        if grid[nn][mm] == 0:
            zeros.append([nn, mm])


def bfs(walls):
    grid_temp = copy.deepcopy(grid)

    for x, y in walls:
        grid_temp[x][y] = 1

    need_visit = copy.deepcopy(virus)

    while need_visit:
        vx, vy = need_visit.pop()
        grid_temp[vx][vy] = 2

        for nx, ny in zip(dx, dy):
            if vx + nx in range(n) and vy + ny in range(m) and grid_temp[vx + nx][vy + ny] == 0:
                need_visit.append([vx + nx, vy + ny])

    result = 0
    for grid_row in grid_temp:
        result += grid_row.count(0)

    return result
 

answer = 0
for comb in list(combinations(zeros, 3)):
    answer = max(bfs(comb), answer)

print(answer)