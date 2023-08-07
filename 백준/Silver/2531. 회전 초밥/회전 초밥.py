import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
menus = []

for _ in range(n):
    menus.append(int(input()))

menus += menus[:k - 1]
answer = 0

for idx1, menu in enumerate(menus[:n]):
    answer = max((len(set(menus[idx1:idx1 + k] + [c]))), answer)

print(answer)