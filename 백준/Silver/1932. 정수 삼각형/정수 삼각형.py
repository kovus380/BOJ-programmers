n = int(input())

triangles = []
for _ in range(n):
    triangles.append(list(map(int, input().split())))

dp = triangles[-1]

triangles.reverse()

for line in triangles[1 : ]:
    
    for idx, point in enumerate(line):
        dp[idx] = max(dp[idx], dp[idx + 1]) + line[idx] 
    
    
print(dp[0])