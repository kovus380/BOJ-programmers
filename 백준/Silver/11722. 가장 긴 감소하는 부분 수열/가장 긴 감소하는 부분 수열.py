n = int(input())

nums = list(map(int, input().split()))
nums.append(0)

answer = [1] * n

for i in range(n):
    temp = [answer[i]]
    for j in range(i):
        if nums[i] < nums[j]:
            temp.append(1 + answer[j])
    answer[i] = max(temp)

print(max(answer))