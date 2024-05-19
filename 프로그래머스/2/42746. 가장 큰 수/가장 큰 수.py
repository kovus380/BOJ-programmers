def solution(numbers):
    answer = ''
    temp_num = []
    for idx, num in enumerate(numbers):
        temp_num.append([str(num) * 6, idx])
    temp_num.sort(reverse=True)
    for num, idx in temp_num:
        answer += str(numbers[idx])
    return str(int(answer))