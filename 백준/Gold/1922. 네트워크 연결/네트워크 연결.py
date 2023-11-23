n = int(input())
m = int(input())

edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])

parents = [i for i in range(n + 1)]

def find_parent(v):
    if parents[v] != v:
        parents[v] = find_parent(parents[v])
    return parents[v]

def union(v1, v2):
    if v1 > v2:
        parents[v1] = v2
    else:
        parents[v2] = v1


answer = 0

for v1, v2, w in edges:
    v1 = find_parent(v1)
    v2 = find_parent(v2)

    if v1 != v2:
        answer += w
        union(v1, v2)

print(answer)