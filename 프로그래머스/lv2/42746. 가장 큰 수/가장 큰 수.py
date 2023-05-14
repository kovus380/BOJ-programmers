def solution(numbers):
    # numbers 원소드를 string 형태로 변환 후 저장
    numbers_str = list(map(str, numbers))
    
    # 원소의 길이가 1,000 이하이기 때문에 비교 시 최소한 3자리로 맞춰야 함 3, 30, 34 -> 333 303030 343434
    numbers_str.sort(key = lambda num : num * 3, reverse = True)
    
    #  numbers_str 내 원소드를 연결, str -> int -> str 형태로 변환
    return str(int(''.join(numbers_str)))