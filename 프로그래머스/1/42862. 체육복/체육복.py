def solution(n, lost, reserve):
    answer = 0
    reserve_set = set()
    lost_set = set()
    
    for student in reserve: 
        reserve_set.add(student)
    for student in lost:
        lost_set.add(student)
    

    for i in range(1, n+1): 
        if i in lost_set: 
            if i in reserve_set: 
                answer += 1 
                reserve_set.remove(i)
            else:                  
                if i-1 in reserve_set:                
                    answer += 1 
                    reserve_set.remove(i-1)
                elif i+1 in reserve_set and i+1 not in lost_set:                    
                    answer += 1 
                    reserve_set.remove(i+1)
        else:
            answer += 1 


                      
    return answer