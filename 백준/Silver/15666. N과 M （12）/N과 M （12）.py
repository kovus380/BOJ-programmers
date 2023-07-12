from collections import deque

m, n = map(int, input().split())

nums = list(map(int, input().split()))

dq = deque([[num] for num in nums])

while len(dq[0]) < n:

    left = dq.popleft()

    for i in nums:
        if left[-1] <= i:
            dq.append(left + [i])

answer = list(dq)
answer.sort()


for idx, value in enumerate(answer):
    if idx == 0:
        print(*value)

    elif answer[idx] != answer[idx - 1]:
        print(*value)
