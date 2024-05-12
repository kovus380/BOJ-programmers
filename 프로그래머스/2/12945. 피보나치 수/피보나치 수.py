def solution(n):
    
    f = [0, 1, 1]
    
    for i in range(2, n):
        f[0], f[1], f[2] = f[1], f[2], ((f[1] + f[2]) % 1234567)
    
    return f[-1]