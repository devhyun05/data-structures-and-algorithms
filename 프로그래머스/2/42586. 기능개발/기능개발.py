from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque(progresses)
    speeds_dq = deque(speeds)
    max_len = len(progresses)
    count = 0

    while dq: 
        for i in range(len(dq)): 
            dq[i] += speeds_dq[i] 
        
        while dq and dq[0] >= 100: 
            dq.popleft()
            speeds_dq.popleft()
            count += 1 
        
        if count > 0: 
            answer.append(count)
            count = 0
            
        
    return answer