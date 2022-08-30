from collections import defaultdict
from functools import reduce
from itertools import combinations
import sys

T = int(input())

for _ in range(T):
    n = int(input())
    group = defaultdict(int)

    for _ in range(n):
        group[input().split()[1]] += 1

    answer = 1


    for g in group.keys():
        answer *= (group[g] + 1)
    
    print(answer - 1)
