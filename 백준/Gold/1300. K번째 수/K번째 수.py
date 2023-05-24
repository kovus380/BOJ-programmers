N = int(input())
k = int(input())

answer = 0
start, end = 1, N * N


while start <= end:
    mid = (start + end) // 2

    small_cnt = 0
    
    for i in range(1, N + 1):
        small_cnt += min(N, mid//i)

    if small_cnt >= k:
        answer = mid
        end = mid - 1
    else : 
        start = mid + 1

print(answer)