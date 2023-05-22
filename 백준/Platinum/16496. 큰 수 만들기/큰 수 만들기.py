N = int(input())

# numbers 원소들을 string 형태로 변환 후 저장
numbers_str = input().split()

# 원소의 길이가 1,000,000,000 이하이기 때문에 비교 시 최소한 9자리로 맞춰야 함 
numbers_str.sort(key = lambda num : num * 9, reverse = True)

#  numbers_str 내 원소드를 연결, str -> int -> str 형태로 변환
print(str(int(''.join(numbers_str))))