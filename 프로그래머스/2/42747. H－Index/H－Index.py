def solution(citations):
    
    citations.sort(reverse=True)
    
    for h in range(len(citations) - 1, -1, -1):
        if citations[h] >= (h + 1):
            return (h + 1)
    
    return 0