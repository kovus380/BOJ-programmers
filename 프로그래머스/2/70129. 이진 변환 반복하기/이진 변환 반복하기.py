def solution(s):
    
    cnt = 0
    rem_zero = 0
    
    while s != "1":
        cnt += 1
        rem_zero += s.count("0")
        s = s.replace("0", "")
        s = str(bin(len(s)))[2:]
        
    return [cnt, rem_zero]