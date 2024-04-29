import heapq

def solution(n, k, enemy):
    answer = 0
    
    attack = []
    
    sum_attack = 0
    
    for idx, e in enumerate(enemy):
        
        heapq.heappush(attack, -e)
        n -= e
        
        while n < 0 and k > 0:
            rem_att = heapq.heappop(attack) * -1
            n += rem_att
            k -= 1
        
        if n < 0:
            return idx
            
    return len(enemy)
            