def solution(nums):
    num_set = set(nums)
    n = len(nums) // 2 
    answer = 0 
    
    if n < len(num_set):
        answer = n
    else:
        answer = len(num_set)
    
    return answer