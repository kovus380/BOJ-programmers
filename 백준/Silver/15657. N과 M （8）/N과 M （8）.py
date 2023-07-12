from collections import deque

m, n = map(int, input().split())

nums = list(map(int, input().split()))

dq = deque([[num] for num in nums])

while len(dq[0]) < n:

    left = dq.popleft()

    for i in nums:
        if i >= left[-1]:
            dq.append(left + [i])

answer = list(dq)
answer.sort()

for value in answer:
    print(*value)
