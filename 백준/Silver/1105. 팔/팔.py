l, r = input().split()

answer = 0

if len(l) == len(r):

    for i in range(len(l)):
        if l[i] == '8' and r[i] == '8':
            answer += 1
        if l[i] != r[i]:
            break

print(answer)