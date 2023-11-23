v, e = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(e)]
parents = [i for i in range(v + 1)]

edges.sort(key=lambda x:x[2])

answer_edges = 0

def find(v):
    if parents[v] == v:
        return v
    else:
        parents[v] = find(parents[v])
        return parents[v]
    
def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    
    if v1 < v2:
        parents[v2] = v1
    else:
        parents[v1] = v2

for v1, v2, w in edges:
    if find(parents[v1]) != find(parents[v2]):
        answer_edges += w
        union(v1, v2)

print(answer_edges)