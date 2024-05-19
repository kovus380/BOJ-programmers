def solution(s):
    answer = []
    tuples = []
    s = s[2:-2].split("},{")
    
    for tup in s:
        tuples.append(list(map(int, tup.split(","))))
        
    tuples.sort(key = lambda x : len(x))
    
    bef_sum = 0
    
    for tup in tuples:
        
        answer.append(sum(tup) - bef_sum)
        bef_sum = sum(tup)
        
    return answer