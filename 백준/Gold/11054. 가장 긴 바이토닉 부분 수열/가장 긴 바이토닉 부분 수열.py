n = int(input())
arr = list(map(int, input().split()))


def find_bitonic(arr):
    dp = [0] * (max(arr) + 1)
    answer = [0] * (len(arr))
    for idx, n in enumerate(arr):
       dp[n] = 1 + max(dp[:n])
       answer[idx] = 1 + max(dp[:n])
    return answer

arr1 = find_bitonic(arr)
arr2 = find_bitonic(arr[::-1])[::-1]

answer = 0 

for i in range(len(arr)):
    answer =  max(arr1[i] + arr2[i] - 1, answer)
print(answer)
