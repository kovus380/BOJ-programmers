from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque()
    q.append([begin])

    while q:
        v = q.popleft()
        if v[-1] == target:
            return(len(v) - 1)
        for word in words:
            new = v[:]
            if word in new:
                continue
            new.append(word)
            if (sum([new[-1][i] != new[-2][i] for i in range(len(begin))])) == 1:
                q.append(new)
    return 0