def solution(participant, completion):
    count_map = {}
    
    for person in participant: 
        count_map[person] = count_map.get(person, 0) + 1 
    
    for person in completion: 
        count_map[person] -= 1 
        
    
    for person, count in count_map.items():
        if count == 1:
            return person 
        
           
    
    
    