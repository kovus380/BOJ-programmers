from collections import defaultdict

computer = [0] * (int(input()) + 1)
line_num = int(input())

line = defaultdict(list)

for _ in range(line_num):
    a, b = map(int, input().split())
    line[a] += [b]
    line[b] += [a]

visit = line[1].copy()

while visit:
    v = visit.pop()
    if not computer[v]:
        computer[v] = 1
        visit += line[v]

print(sum(computer) - 1)
