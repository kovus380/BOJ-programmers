N, M = map(int, input().split())

nums = []

board_input = []

for _ in range(N):
    board_input.append(input())

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board_input[x][y] != 'W' : first_W += 1
                else:
                    if board_input[x][y] != 'B' : first_W += 1
        nums.append(first_W)
        nums.append(64 - first_W)

print(min(nums))