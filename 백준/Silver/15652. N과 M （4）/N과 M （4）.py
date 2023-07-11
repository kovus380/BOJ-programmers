from collections import deque

m, n = map(int, input().split())

dq = deque([[i] for i in range(1, m + 1)])

num = [i for i in range(1, m + 1)]

depth = 0

while len(dq[0]) < n:

    left = dq.popleft()

    for i in num:
        
        if i >= left[-1]:
            dq.append(left + [i])

for value in dq:
    print(*value)
