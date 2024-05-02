def solution(arr):
    nums = []
    opers = []
    
    for a in arr:
        if a.isdigit():
            nums.append(int(a))
        else:
            opers.append(a)
        
    N = len(nums)
    
    
    dp_min = [[float('inf')] * N for _ in range(N)]
    dp_max = [[float('-inf')] * N for _ in range(N)]

    
    
    for length in range(N):
        for start in range(N - length):
            end = start + length
            
            if start == end:
                dp_min[start][end] = dp_max[start][end] = nums[start]
                continue
                
            for inter in range(start, end):
                
                if opers[inter] == '+': 
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][inter] + dp_max[inter + 1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][inter] + dp_min[inter + 1][end])
                else:
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][inter] - dp_min[inter + 1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][inter] - dp_max[inter + 1][end])
                
    
    return dp_max[0][-1]