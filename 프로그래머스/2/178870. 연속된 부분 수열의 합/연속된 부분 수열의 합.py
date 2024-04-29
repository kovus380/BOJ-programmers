def solution(sequence, k):
    answer = []
    rev_seq = sequence[::-1]
    rev_sum = [0]
    
    for num in rev_seq:
        rev_sum.append(rev_sum[-1] + num)
        
    for i in range(len(rev_seq)): # i는 간격 (사이 개수)
        answer = []
        if rev_sum[i + 1] < k:
            continue
        for j in range(1, len(rev_seq) - i + 1): # j 는 시작 지점, 큰 곳부터 시작
            if (rev_sum[j + i] - rev_sum[j - 1]) == k:
                answer = [len(rev_seq) - (j+i), len(rev_seq) - j]
            elif (rev_sum[j + i] - rev_sum[j - 1]) < k:
                break
                
        if answer:
            return answer
    return answer