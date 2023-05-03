def solution(triangle):
    answer = 0
    top_sum = [triangle[0][0]]
    for idx1, t in enumerate(triangle[1:]):
        tmp_sum = []
        for idx2, val in enumerate(t):
            if (idx2 == 0):
                tmp_sum.append(top_sum[0] + val)
            elif (idx2 == len(t) - 1):
                tmp_sum.append(top_sum[-1] + val)
            else:
                tmp_sum.append(max([top_sum[idx2 - 1] + val, top_sum[idx2] + val]))
        top_sum = tmp_sum
    return max(top_sum)