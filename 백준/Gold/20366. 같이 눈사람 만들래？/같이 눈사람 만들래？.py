n = int(input())

snows = list(map(int, input().split()))

snows.sort()

answer = snows[-1] + snows[-2]

for i in range(n - 3):
    for j in range(i + 3, n):

        start, end = i + 1, j - 1
        
        while start < end:
            
            tmp = (snows[j] + snows[i]) - (snows[end] + snows[start])

            answer = min(abs(tmp), answer)

            if answer == 0:
                print(answer)
                exit()

            if tmp >= 0:
                start += 1
            else:
                end -= 1


print(answer)