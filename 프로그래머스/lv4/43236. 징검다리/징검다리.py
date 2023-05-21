def solution(distance, rocks, n):
    
    left, right = 0, distance
    # rocks의 마지막 돌과 도착 돌 사이의 거리도 고려해야 함
    rocks.append(distance)
    rocks.sort()
    
    while left <= right:
        mid = (left + right) // 2
        
        # 제거한 돌의 개수
        del_stones_cnt = 0
        # 거리를 잴 바로 이전의 돌
        pre_stone = 0
        
        for rock in rocks:
            # 이전의 돌과의 거리가 mid 값보다 작다면
            if (rock - pre_stone) < mid:
                del_stones_cnt += 1 # 돌을 제거함
            else: # 이전의 돌과의 거리가 mid 보다 크거나 같다면 해당 돌을 이후의 돌과 비교하도록 pre_stone 으로 지정
                pre_stone = rock
            # 만약 제거한 돌이 n보다 크다면 더이상 돌 필요가 없음    
            if del_stones_cnt > n:
                break
        
        # 만약 제거한 돌이 n보다 크다면 mid 값을 줄여야 함
        if del_stones_cnt > n:
            right = mid - 1
        
        # 만약 제거한 돌이 n보다 작거나 같다면 mid 값을 늘려도 됨 (만족한다)
        else:
            left = mid + 1
            
    return right