from collections import defaultdict

def solution(N, number):

    ddict = defaultdict(list)
    ddict[1] += [N]
    cnt = 1
    
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
        
    return -1
