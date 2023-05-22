N, C = map(int, input().split())

routers = []

for _ in range(N):
    routers.append(int(input()))

routers.sort()

answer = 0
left, right = 1, routers[-1] - routers[0]

while left <= right:
    mid = (left + right) // 2
    before = routers[0]
    using = 1

    for i in range(1, len(routers)):
        if routers[i] - before >= mid:
            before = routers[i]
            using += 1

    if using >= C:
        left = mid + 1

    else :
        right = mid - 1


print(right)
