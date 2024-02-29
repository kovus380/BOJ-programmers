from collections import deque

def solution(priorities, location):
    dq = deque() 

    locations = [0 for _ in range(len(priorities))]

    for i in range(len(priorities)):
        dq.append([i, priorities[i]])

    # dq =  [(i,p) for i,p in enumerate(priorities)]

    
    order = 1

    while (locations[location] == 0):
        left = dq.popleft()
        
        if len(dq) == 0:
            locations[left[0]] = order
            break


        temp_max = max(dq, key= lambda x: x[1])

        if left[1] >= temp_max[1]:
            locations[left[0]] = order
            order += 1

        else:
            dq.append(left)
    
    return locations[location]

""" 
def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor%jobs]:
            priorities[cursor%jobs] = 0
            answer += 1
            if cursor%jobs == location:
                break
        cursor += 1   
    return answer
 """