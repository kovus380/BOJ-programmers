N, M =  map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    
    mid = (start + end) // 2

    tree_sum = 0
    for tree in trees:
        if (tree > mid):
            tree_sum += (tree - mid)

    if tree_sum >= M:
        start = mid + 1

    else:
        end = mid - 1

print(end)