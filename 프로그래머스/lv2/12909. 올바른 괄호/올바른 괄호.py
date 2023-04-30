def solution(s):
    answer = True
    cnt = 0
    s = list(s)
    while s:
        tmp = s.pop()
        if tmp == '(':
            if cnt > 0:
                cnt -= 1
            else:
                return False
        else:
            cnt += 1
    if cnt:
        return False
    return True