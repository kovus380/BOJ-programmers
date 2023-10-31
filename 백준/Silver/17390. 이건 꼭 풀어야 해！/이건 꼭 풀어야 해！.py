import sys

n, q = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))

sums = [0]
for i in range(n):
    sums.append(sums[i] + a[i])

for _ in range(q):
    start, end = map(int, sys.stdin.readline().split())
    print(sums[end] - sums[start - 1])