def solution(n, computers):
    answer = 0
    connect = {}
    for num, computer in enumerate(computers):
        tmp = []
        for idx, val in enumerate(computer):
            if val and idx != num:
                tmp.append(idx)
        connect[num] = tmp
   
    visited = [0] * n

    for i, v in enumerate(visited):
        if v == 1:
            continue
        visit = connect[i]
        visited[i] = 1
        while visit:
            v_pop = visit.pop()
            if visited[v_pop] == 1:
                continue
            visit += connect[v_pop]
            visited[v_pop] = 1
        answer += 1
    
    return answer
