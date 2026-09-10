def solution(arr, divisor):
    answer = []
    n = len(arr)
    
    for i in range(n): 
        if arr[i] % divisor == 0: 
            answer.append(arr[i])
    
    if len(answer) == 0: 
        answer.append(-1)
    else:
        answer.sort()
    return answer