T = int(input())

for _ in range(T):
    num = int(input())
    cnt = [0, 0]
    if num == 0:
        cnt[0] += 1
    elif num == 1:
        cnt[1] += 1
    else:
        bb = [1, 0]
        b = [0, 1]
        for i in range(2, num + 1):
            bb, b = b, [bb[0] + b[0], bb[1] + b[1]]
        cnt = b
    print(cnt[0], cnt[1])