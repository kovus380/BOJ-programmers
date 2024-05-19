import string

def solution(s, skip, index):

    answer = ''
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    for _skip in skip:
        letters = letters.replace(_skip, "")
    
    l_len = len(letters)
    
    for char in list(s):
        answer += letters[(letters.find(char) + index) % l_len]
    
    return answer