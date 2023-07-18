from collections import deque

a, b = map(int, input().split())

visited = deque([[a, 0]])
flag = False

while visited:
    value, depth = visited.pop()
    
    if value > b:
        continue

    if value == b:
        print(depth + 1)
        flag = True
    
    visited.append([value * 2, depth + 1])
    visited.append([int(str(value) + "1"), depth + 1])

if not flag:
    print(-1)