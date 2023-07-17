n = int(input())

array = [0, 1]

for i in range(2, n + 1):
    array[0], array[1] = array[1], array[0] + array[1]

print(array[-1])