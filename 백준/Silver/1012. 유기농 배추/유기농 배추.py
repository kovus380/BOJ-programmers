def dfs(x, y, field):
    if (x >= len(field[0])) or (x < 0) or (y >= len(field)) or (y < 0) or (field[y][x] == 0):
        return
    
    field[y][x] = 0

    dfs(x + 1, y, field)
    dfs(x - 1, y, field)
    dfs(x, y + 1, field)
    dfs(x, y - 1, field)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for i in range(N)]
    count = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
        
    count = 0
    for y in range(N):
        for x in range(M):
            if (field[y][x] == 1):
                count += 1
                dfs(x, y, field)

    print(count)

