def solution(arr):
    answer = []
    prev_num = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] != prev_num: 
            answer.append(prev_num)
            prev_num = arr[i]
            
    answer.append(arr[-1])
    
    return answer