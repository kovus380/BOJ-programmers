import sys
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())

count = 0

while n >= 0:

    n -= 1
    
    if ((2 ** n) - 1) >= r:
        if ((2 ** n) - 1) >= c: # 1번
            pass

        else:
             # 2번
            count += ((2 ** n) * (2 ** n))
            c -= (2 ** (n))

    else:
        if (((2 ** n)) - 1) >= c: # 3번
            count += (((2 ** n) * (2 ** n))) * 2
            r -= (2 ** (n))

        else:
            count += (((2 ** n) * (2 ** n))) * 3
            r -= (2 ** (n))
            c -= (2 ** (n)) # 4번

print(int(count))