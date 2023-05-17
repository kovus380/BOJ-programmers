def solution(citations):
    citations.sort()
    for i in range(len(citations), 1, -1):
        if i <= citations[len(citations) - i]:
            return i
    return 0