n = int(input())

time_array = [list(map(int, input().split())) for _ in range(n)]
time_array.sort()

office = [time_array[0]]

for start, end in time_array[1:]:
    if office[-1][1] > end :
        office.pop()
        office.append([start, end])

    elif office[-1][1] <= start:
        office.append([start, end])

print(len(office))