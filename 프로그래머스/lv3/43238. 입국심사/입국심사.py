
def solution(n, times):
    answer = 0
    left, right = min(times), max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        total_person = 0
        for time in times:
            total_person += mid // time
        
        if total_person >= n:
            answer = mid
            right = mid - 1
        elif total_person < n:
            left = mid + 1
        
    return answer