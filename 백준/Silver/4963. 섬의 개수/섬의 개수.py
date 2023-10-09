import sys
sys.setrecursionlimit(10 ** 6)

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def dfs(x, y):

    if grids[x][y] == 0:
        return
    
    grids[x][y] = 0
    
    for nx, ny in zip(dx, dy):
        nx += x
        ny += y
        if nx in range(0, h) and ny in range(0, w) and grids[nx][ny] == 1:
            dfs(nx, ny)
    
    return




while True:
    w, h = map(int, input().split())

    if (w == 0) and (h == 0):
        break

    grids = []
    

    for _ in range(h):
        grids.append(list(map(int, input().split())))

    
    answer = 0

    for x in range(h):
        for y in range(w):
            if grids[x][y] == 1:
                dfs(x, y)
                answer += 1

    print(answer)
    


    

