def solution(arr):
    min_num = min(arr)
    answer = []
    
    for num in arr: 
        if num != min_num: 
            answer.append(num)
    
    if not answer: 
        answer.append(-1)
        
    return answer