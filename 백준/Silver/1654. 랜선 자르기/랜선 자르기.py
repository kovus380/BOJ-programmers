N, K = map(int, input().split())
lines = []
for _ in range(N):
    lines.append(int(input()))

start = 1
end = sum(lines) // K

while start <= end:
    mid = (start + end) // 2
    
    line_count = 0

    for line in lines:
        line_count += (line // mid)

    if line_count >= K:
        start = mid + 1
    else :
        end = mid - 1

print(end)