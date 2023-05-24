N = int(input())
A = list(map(int, input().split()))

small_same = [1] * N

for i in range(N - 1, -1, -1):
    temp = [0]
    for j in range(i + 1, N):
        if A[i] < A[j]:
            temp.append(1 + small_same[j])
    small_same[i] = max(temp)

print(max(small_same) + 1)