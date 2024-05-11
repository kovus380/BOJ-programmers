from collections import Counter

def solution(X, Y):
    X = Counter(X)
    Y = Counter(Y)
    
    answer = []
    
    for i in range(9, -1, -1):
        i = str(i)
        a = i * min(X[i], Y[i])
        if a:
            answer.append(a)
        
    if not answer:
        return "-1"
    elif answer[0].startswith("0"):
        return "0"
    else: 
        return ''.join(answer)
    