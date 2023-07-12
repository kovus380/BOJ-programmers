from itertools import permutations

n, m = map(int, input().split())

nums = list(map(int, input().split()))

per = sorted(list(map(list, list(permutations(nums, m)))))

for p in per:
    print(*p)