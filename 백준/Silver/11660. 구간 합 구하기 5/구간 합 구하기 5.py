import sys

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

sums = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    temp = [0]
    for j in range(n):
        temp.append(temp[-1] + grid[i][j])
        sums[i+1][j+1] = sums[i][j+1] + temp[-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1])


