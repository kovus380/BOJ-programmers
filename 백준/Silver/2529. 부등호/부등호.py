n = int(input())

signs = input().split()

# print(signs)
def valid(exp, i, start):
    # print(exp, i)
    if (i == (n + 1)):
        return exp
    
    for j in range(start[0], start[1], start[2]):
        if j not in exp:
            # print(j, exp[-1], i)
            if (signs[i - 1] == '>' and (exp[-1] > j) or (signs[i - 1] == '<' and (exp[-1] < j))):    
                # print(111111111)
                ret = valid(exp + [j], i + 1, start)
                if ret:
                    return ret

for s in range(9, -1, -1):
    ret = valid([s], 1, [9, -1, -1])
    if ret:
        print(''.join(map(str, ret)))
        break

for s in range(10):
    ret = valid([s], 1, [0, 10, 1])
    if ret:
        print(''.join(map(str, ret)))
        break