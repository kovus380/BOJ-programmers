n = int(input())

stairs = [0, 0, 0]

for _ in range(n):
    stairs.append(int(input()))

dp = [0] * len(stairs)

for i in range(3, len(stairs)):
    dp[i] = max(dp[i - 3] + stairs[i - 1], dp[i - 2]) + stairs[i]

print(dp[-1])