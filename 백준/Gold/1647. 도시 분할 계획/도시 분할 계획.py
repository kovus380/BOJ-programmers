import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])

parents = [i for i in range(n+1)]

def find_parents(v):
    if parents[v] != v:
        parents[v] = find_parents(parents[v])
    return parents[v]

def union(v1, v2):
    if v1 > v2:
        parents[v1] = v2
    else:
        parents[v2] = v1

answer = []

for v1, v2, w in edges:
    if len(answer) == (n-2):
        break

    v1 = find_parents(v1)
    v2 = find_parents(v2)

    if v1 != v2:
        union(v1, v2)
        answer.append(w)

print(sum(answer))