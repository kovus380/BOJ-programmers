from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    
    ref = defaultdict(str)
    profit = defaultdict(int)
    
        
    for idx in range(len(referral)):
        ref[enroll[idx]] = referral[idx]
    
    have_to_visit = [[seller[idx], a * 100] for idx, a in enumerate(amount)]
    
        
    while have_to_visit:
        
        name, won = have_to_visit.pop()
        
        if  won < 10:
            profit[name] += won
            continue
            
        else:
            profit[name] += won - int(won * 0.1)
        if name == '':
            continue
        
        have_to_visit.append([ref[name], int(won * 0.1)])
        
    return [profit[e] for e in enroll]