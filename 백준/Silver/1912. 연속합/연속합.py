n = int(input())
nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    nums[i] = max(nums[i - 1] + nums[i], nums[i])

print(max(nums))