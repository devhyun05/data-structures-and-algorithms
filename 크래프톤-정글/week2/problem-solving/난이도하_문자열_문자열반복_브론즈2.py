# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

# import sys 
# input = sys.stdin.readline 

# n = int(input())

# for _ in range(n):
#     repeated_times, s = input().split()
#     new_s = ""
    
#     for c in s: 
#         new_s += c * int(repeated_times)
       
#     print(new_s)

# 테스트 케이스의 개수 

T = int(input())

for _ in range(T):
    repeated_times, s = input().split()
    res = ""
    for c in s:
        res += c * int(repeated_times)
    
    print(res)