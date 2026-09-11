def solution(numbers):
    n = len(numbers)
    num_set = set()
    
    for i in range(n):
        for j in range(i+1, n): 
            num_set.add(numbers[i] + numbers[j]) 
            
    answer = list(num_set)
    answer.sort()
    
    return answer