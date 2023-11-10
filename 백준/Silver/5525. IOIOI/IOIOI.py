n = int(input())
m = int(input())
s = input()

answer, cur, cnt = 0, 0, 0

while cur < (m - 2):

    if s[cur: cur + 3] == "IOI":
        cnt += 1
        cur += 2

    else:
        cur += 1
        cnt = 0
    
    if cnt == n:
        answer += 1
        cnt -= 1

print(answer)