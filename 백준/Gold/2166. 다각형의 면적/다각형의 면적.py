n = int(input())

dots = [list(map(int, input().split())) for _ in range(n)]

dots.append(dots[0])
    
answer = 0
for i in range(1, n + 1):
    answer += (dots[i - 1][0] * dots[i][1] - dots[i][0] * dots[i - 1][1])

answer /= 2
answer = abs(answer)
print(float(answer))