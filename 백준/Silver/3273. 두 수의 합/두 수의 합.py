n = int(input())

arr = list(map(int, input().split()))
arr.sort()

x = int(input())
exists = [0] * (2000000 + 1)

for a in arr:
    exists[a] = 1

answer = 0

for a in arr:
    if (x - a) - a <= 0:
        break
    if exists[x - a] == 1:
        answer += 1

print(answer)