n = int(input())

dp = [1, 2]

for i in range(2, n):
    dp.append((dp[i - 2] + dp[i - 1]) % 10007)

print(dp[n - 1])