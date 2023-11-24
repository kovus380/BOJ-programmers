def cal_dist(v1, v2):
    return round(((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2) ** (1/2), 2)


n = int(input())
edges = []
stars = [list(map(float, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        edges.append([i, j, cal_dist(stars[i], stars[j])])

edges.sort(key=lambda x:x[2])

parents = [i for i in range(n)]

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
    v1 = find_parent(parents[v1])
    v2 = find_parent(parents[v2])

    if v1 != v2:
        union(v1, v2)
        answer += w

print(answer)