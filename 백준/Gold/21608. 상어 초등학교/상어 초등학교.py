from collections import defaultdict


n = int(input())
couples = defaultdict(list)

answer = [[0] * n for _ in range(n)]
visited = [[-1, -1]] * (n*n + 1)

for i in range(n*n):
    tmp = list(map(int, input().split()))
    couples[tmp[0]] = tmp[1:]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for key, value in couples.items():

    # print("===========================")
    # print(key, value)
    # print(answer)
    # print(visited)


    # visited[key] = 1 # 방문 했음을 알림

    tmp_grid = [[-1] * n for _ in range(n)]

    # visited[1] = [1, 1]

    # 선호하는 칸

    for v in value:
        x, y = visited[v]

        if [x, y] != [-1, -1]:

            for nx, ny in zip(dx, dy):
                if (x + nx) in range(n) and (y + ny) in range(n) and answer[x + nx][y + ny] == 0:
                    tmp_grid[x + nx][y + ny] += 1

    loc = max(map(max, tmp_grid))

    max_list = [(i,j) for i in range(n) for j in range(n) if tmp_grid[i][j]==loc and answer[i][j] == 0]
    

    # print(11111111, max_list)
    if len(max_list) == 1:
        answer[max_list[0][0]][max_list[0][1]] = key
        visited[key] = [max_list[0][0], max_list[0][1]]
        continue


    # 비어있는 칸 많은 칸

    tmp_max = [-1] * len(max_list)

    for idx, (x, y) in enumerate(max_list):
        
        for nx, ny in zip(dx, dy):
            
            if (x + nx) in range(n) and (y + ny) in range(n) and answer[x+nx][y+ny] == 0:
                # print(idx, x + nx, y + ny)
                tmp_max[idx] += 1

    # print(555555555, tmp_max)
    loc = max(tmp_max)

    # print("loc", tmp_max[4], loc, tmp_max[4] == loc, max_list[4])

    max_list2 = [max_list[i] for i in range(len(tmp_max)) if tmp_max[i] == loc]
    # print(4444444, loc, max_list2)

    for tx, ty in max_list2:
        if answer[tx][ty] == 0:
            answer[max_list2[0][0]][max_list2[0][1]] = key
            visited[key] = [max_list2[0][0], max_list2[0][1]]
    # print(2222, answer)



# print(answer)

result = 0
for x in range(n):
    for y in range(n):
        like = 0
        for nx, ny in zip(dx, dy):
            if (x + nx) in range(n) and (y + ny) in range(n) and answer[x+nx][y+ny] in couples[answer[x][y]]:
                like += 1
        if like != 0:
            result += (10**(like-1))

print(result)