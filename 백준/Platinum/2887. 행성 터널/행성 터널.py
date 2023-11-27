import sys

input = sys.stdin.readline
n = int(input())

edges = []
x_dots, y_dots, z_dots = [], [], []

for i  in range(n):
    x, y, z = map(int, input().split())
    x_dots.append([x, i])
    y_dots.append([y, i])
    z_dots.append([z, i])

x_dots.sort()
y_dots.sort()
z_dots.sort()

parents = [i for i in range(n)]

for i in range(1, n):
    edges.append([x_dots[i][0] - x_dots[i - 1][0], x_dots[i][1], x_dots[i - 1][1]])
    edges.append([y_dots[i][0] - y_dots[i - 1][0], y_dots[i][1], y_dots[i - 1][1]])
    edges.append([z_dots[i][0] - z_dots[i - 1][0], z_dots[i][1], z_dots[i - 1][1]])

edges.sort()

def find_parent(v):
    if v != parents[v]:
        parents[v] = find_parent(parents[v])
    return parents[v]

answer = 0

for w, v1, v2 in edges:
    v1 = find_parent(parents[v1])
    v2 = find_parent(parents[v2])

    if v1 != v2:
        if v1 > v2:
            parents[v1] = v2
        else:
            parents[v2] = v1
        answer += w

print(answer)
