import heapq
from heapq import heapify

def solution(jobs):
    now, bef = 0, -1
    times = []
    heap = []
    
    while len(times) < len(jobs):
        for job in jobs:
            if now >= job[0] > bef:
                heapq.heappush(heap, [job[1], job[0]])
            
        if len(heap) != 0:
            x, y = heapq.heappop(heap)
            bef = now
            now += x
            times.append(now - y)
        else:
            now += 1
            
    return sum(times) // len(times)
            