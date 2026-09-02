from collections import deque 

def solution(priorities, location):
    queue = deque()
    count = 0 
    
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
        
    answer = queue[location][1]   
    
    while queue: 
        current = queue[0][0]
        higher_priority_found = False 
        
        for process in queue: 
            if process[0] > current: 
                higher_priority_found = True         
                break 
                
        temp = (0, 0)
        
        if higher_priority_found: 
            queue.append(queue.popleft())
        else: 
            temp = queue.popleft()
            count += 1 
      
        if not higher_priority_found and temp[1] == answer: 
            break 
            
    return count 