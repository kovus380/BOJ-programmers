n = int(input())
parents = list(map(int, input().split()))
rem_node = int(input())

def dfs(delete, parents):
    parents[delete] = -2

    for i in range(n):
        if (parents[i] == delete):
            dfs(i, parents)
    

dfs(rem_node, parents)

leaf_cnt = 0

for i in range(n):
    if (parents[i] != -2) and (i not in parents):
        leaf_cnt += 1

print(leaf_cnt)