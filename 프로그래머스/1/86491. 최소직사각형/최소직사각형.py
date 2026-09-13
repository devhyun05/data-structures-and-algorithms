def solution(sizes):
    n = len(sizes)
    vertical_max = 0 
    horizontal_max = 0 
    answer = float('-inf')
    
    for i in range(n):
        if sizes[i][0] > horizontal_max: 
            horizontal_max = sizes[i][0]
        if sizes[i][1] > vertical_max:
            vertical_max = sizes[i][1]
    
    
    
    for i in range(n):
        vertical_cal = horizontal_max * min(sizes[i][0], sizes[i][1])
        horizontal_cal = vertical_max * min(sizes[i][0], sizes[i][1]) 
        answer = max(answer, max(vertical_cal, horizontal_cal))
    
               
    return answer