import heapq
from heapq import heapify

def solution(scoville, K):
    cnt = 0
    heapify(scoville)
    while scoville:
        if scoville[0] >= K:
            return cnt
        if len(scoville) <= 1:
            return -1
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + 2 * b)
            cnt += 1
    
    return -1