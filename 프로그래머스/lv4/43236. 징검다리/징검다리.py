def solution(distance, rocks, n):
    
    left, right = 0, distance
    rocks.append(distance)
    rocks.sort()
    
    while left <= right:
        mid = (left + right) // 2
        del_stones_cnt = 0
        pre_stone = 0
        
        for rock in rocks:
            if (rock - pre_stone) < mid:
                del_stones_cnt += 1
            else:
                pre_stone = rock
                
            if del_stones_cnt > n:
                break
                
        if del_stones_cnt > n:
            right = mid - 1
            
        else:
            left = mid + 1
            
    return right