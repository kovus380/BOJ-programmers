import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
menus = []

for _ in range(n):
    menus.append(int(input()))

menus += menus[:k - 1]
counts = [0] * (d + 1)

temp = menus[ : k]
set_len = 0
for t in temp:
    if counts[t] == 0:
        set_len += 1
    counts[t] += 1


answer = 0

for idx, menu in enumerate(menus[k:]):

    counts[menus[idx]] -= 1
    if not counts[menus[idx]]:
        set_len -= 1
    
    if not counts[menu]:
        set_len += 1
    
    counts[menu] += 1

    answer = max(answer, set_len + (counts[c] == 0))

    
print(answer)
