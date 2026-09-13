# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

import math 

def is_prime(n): 
    if n < 2: 
        return False 
    
    if n == 2:
        return True 
    
    if n % 2 == 0:
        return False 
    
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        if n % i == 0:
            return False 
    
    return True 

num_count = int(input())
nums = list(map(int, input().split())) 
ans = 0 

for i in range(num_count):
    if is_prime(nums[i]): 
        ans += 1

print(ans)

