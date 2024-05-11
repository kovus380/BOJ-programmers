from collections import Counter

def solution(k, tangerine):
    
    
    answer = 0
    cnt = 0
    
    tan_c = sorted(Counter(tangerine).items(), key=lambda x: x[1], reverse=True)
    
    for tan in tan_c:
        answer += 1
        cnt += tan[1]
        if cnt >= k:
            break
    
    return answer