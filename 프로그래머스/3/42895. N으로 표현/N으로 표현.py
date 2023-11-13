from collections import defaultdict

def solution(N, number):
    answer = 0
    ddict = defaultdict(list)
    ddict[1] += [N]
    cnt = 1
    
    before = [N]
    next_visit = []
    visited = [0] * 32000
    
    if N == number:
        return 1

    while cnt < 8:
        cnt += 1
        bef = ddict[cnt - 1][0]
        ddict[cnt] += [bef * 10 + N]
        for i in range(1, cnt):
            for a in ddict[i]:
                for b in ddict[cnt - i]:
                    ddict[cnt] += [a + b, a - b, a * b]
                    if b != 0:
                        ddict[cnt] += [a // b]
        
        if number in ddict[cnt]:
            return cnt
        
        # ddict[cnt] = list(set(ddict[cnt]))
        
    return -1
