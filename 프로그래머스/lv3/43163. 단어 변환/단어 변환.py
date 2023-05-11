from collections import deque


def solution(begin, target, words):
    # target 값이 word에 없는 경우 바로 return (속도)
    if target not in words:
        return 0
    q = deque()
    q.append([begin])

    # bfs
    while q:
        v = q.popleft()

        # v[-1] 이 target인 경우 답!! return
        if v[-1] == target:
            return(len(v) - 1)
        
        for word in words:
            # v값 영향가지 않도록 값만 복사
            tmp = v[:]

            # 현재 방문할 word가 이미 방문한 tmp(v)에 있다면 pass
            if word in tmp:
                continue

            # 바로 이전의 값과 현재 삽입할 word가 한 글자만 다른지 확인
            if (sum([tmp[-1][i] != word[i] for i in range(len(begin))])) == 1:
                q.append(tmp + [word])
    return 0
