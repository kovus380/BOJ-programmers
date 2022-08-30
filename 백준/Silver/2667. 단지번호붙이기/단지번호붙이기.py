N = int(input())

maps = []

for _ in range(int(N)):
    maps.append(list(input()))
    
def dfs(x, y, cnt):
    if (x >= len(maps)) or (x < 0) or (y >= len(maps[0])) or (y < 0) or (maps[x][y] == '0'):
        return 0
    
    cnt += 1
    maps[x][y] = '0'

    return cnt + dfs(x + 1, y, 0) + dfs(x - 1, y, 0) + dfs(x, y + 1, 0) + dfs(x, y - 1, 0)

count = 0
houses = []

for x in range(len(maps)):
    for y in range(len(maps[0])):
        if maps[x][y] != "0":
            count += 1
            houses.append(dfs(x, y, 0))

print(count)
print('\n'.join(str(v) for v in sorted(houses)))