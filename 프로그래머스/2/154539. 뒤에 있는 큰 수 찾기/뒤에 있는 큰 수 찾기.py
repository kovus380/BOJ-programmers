def solution(numbers):
    
    answer = [0] * len(numbers)
    stack = []
    
    for idx, num in enumerate(numbers):
        while stack and num > numbers[stack[-1]]:
            p = stack.pop()
            answer[p] = num
        stack.append(idx)
        
    while stack:
        answer[stack.pop()] = -1
        
    return answer