from collections import defaultdict

N, M = map(int, input().split())

pair = defaultdict()

for _ in range(N):
    address, pw = input().split()
    pair[address] = pw

for _ in range(M):
    print(pair[input()])