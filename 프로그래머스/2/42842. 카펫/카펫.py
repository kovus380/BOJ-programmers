def solution(brown, yellow):
    
    area = brown + yellow
    
    for num in range(int((area) * 0.5), 0, -1):
        
        if area % num != 0:
            continue
            
        if ((num + area // num) * 2 - 4) == brown:
            return [num, area // num]