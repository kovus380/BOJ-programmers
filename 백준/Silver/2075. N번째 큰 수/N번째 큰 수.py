import sys, heapq

n = int(input())

heap = [-(sys.maxsize + 1)] * n

for _ in range(n):
    for num in list(map(int, input().split())):
        heapq.heappush(heap, max(heapq.heappop(heap), num))

print(heapq.heappop(heap))