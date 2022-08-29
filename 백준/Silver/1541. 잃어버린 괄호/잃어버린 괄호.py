from collections import deque
import re

answer = 0
exp = deque(input())
sign = '+'

while exp:
    num = exp.popleft()
    while exp and exp[0].isdigit():
        num += exp.popleft()

    answer += int(sign + num)
    
    if exp and (exp.popleft() == '-'):
        sign = '-'
        
print(answer)
