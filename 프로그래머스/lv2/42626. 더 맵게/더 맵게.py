import heapq
from heapq import heapify

def solution(scoville, K):
        answer = 0
        heapify(scoville)
        while scoville:
            
            if scoville[0] >= K:
                return answer
            elif len(scoville) <= 1:
                return -1
            else:
                a = heapq.heappop(scoville)
                b = heapq.heappop(scoville)
                heapq.heappush(scoville, a + b*2)
                answer += 1