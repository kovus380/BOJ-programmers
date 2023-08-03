N = int(input())

dp = [0]

for _ in range(N):
    num = float(input())
    dp.append(max(dp[-1] * num, num))

print('%0.3f' % max(dp))