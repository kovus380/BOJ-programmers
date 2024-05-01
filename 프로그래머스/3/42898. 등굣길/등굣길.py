def solution(m, n, puddles):
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    
    for y, x in puddles:
        grid[x][y] = False
        
    grid[0][1] = 1
    
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if grid[x][y] is not False:
                grid[x][y] = grid[x-1][y] + grid[x][y-1]
        
    return grid[-1][-1] % 1000000007