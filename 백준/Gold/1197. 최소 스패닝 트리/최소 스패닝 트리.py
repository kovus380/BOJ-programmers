v, e = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(e)]
parents = [i for i in range(v + 1)]

edges.sort(key=lambda x:x[2])

answer_edges = 0


def find_parent(v):
    if parents[v] != v:
        parents[v] = find_parent(parents[v])
    return parents[v]

def union(v1, v2):
    v1 = find_parent(v1)
    v2 = find_parent(v2)

    if v1 > v2:
        parents[v1] = v2
    else:
        parents[v2] = v1



for v1, v2, w in edges:
    if find_parent(v1) != find_parent(v2):
        answer_edges += w
        union(v1, v2)

print(answer_edges)