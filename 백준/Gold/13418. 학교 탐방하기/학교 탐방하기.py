import sys
input = sys.stdin.readline

n, m = map(int, input().split())

uphill, downhill = [], []
max_uphill, min_uphill = 0, 0

one = list(map(int, input().split()))

for _ in range(m):
    tmp = list(map(int, input().split()))
    
    if tmp[-1] == 0:
        uphill.append(tmp)
    else:
        downhill.append(tmp)

def find_parents(v):
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]

def union(v1, v2):
    if v1 > v2:
        parents[v1] = v2
    else:
        parents[v2] = v1
    

def find_path(updownlist):
    result = []
    for v1, v2, updown in updownlist:
        
        if len(result) == (n - 1):
            break

        v1 = find_parents(parents[v1])
        v2 = find_parents(parents[v2])


        if v1 != v2:
            union(v1, v2)
            result.append(1 if updown == 0 else 0) 
     
    return sum(result)

parents = [i for i in range(n + 1)]
max_uphill = find_path(uphill + downhill)

parents = [i for i in range(n + 1)]
min_uphill = find_path(downhill + uphill)

max_uphill += (1 if one[-1] == 0 else 0)
min_uphill += (1 if one[-1] == 0 else 0)

print(max_uphill**2 - min_uphill**2)