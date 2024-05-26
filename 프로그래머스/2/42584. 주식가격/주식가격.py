def solution(prices):
    stack = []
    
    for i in range(len(prices)):
        s = 0
        for j in range(i + 1, len(prices)):
            
            s += 1
            if prices[i] > prices[j]:
                break

        stack.append(s)
        
    return stack
        