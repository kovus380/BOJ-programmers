def solution(money):
    
    dp1 = money[:-1] # 첫번째 원소가 포함된 경우
    dp1[2] = dp1[2] + dp1[0]
    
    for i in range(3, len(dp1)):
        dp1[i] = dp1[i] + max(dp1[i - 2], dp1[i - 3])
        
    
    dp2 = money[1:] # 첫번째 원소가 제거된 경우
    dp2[2] = dp2[2] + dp2[0]
    
    for i in range(3, len(dp1)):
        dp2[i] = dp2[i] + max(dp2[i - 2], dp2[i - 3])
        
        
    return max(max(dp1), max(dp2))