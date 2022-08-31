import sys

N, M = map(int, input().split())
name_to_num = {}
num_to_name = {}

for i in range(1, N + 1):
    name = sys.stdin.readline().split()[0]
    name_to_num[name] = i
    num_to_name[i] = name


for _ in range(M):
    q = sys.stdin.readline().split()[0]
    print(num_to_name[int(q)] if q.isdigit() else name_to_num[q])