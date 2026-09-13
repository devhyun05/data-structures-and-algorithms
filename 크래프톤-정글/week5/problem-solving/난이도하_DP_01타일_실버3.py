# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

# 시간 초과 
N = int(input())

if N < 3:
    print(N)
else:
    num_1 = 1 
    num_2 = 2 
    ans = 0 

    for i in range(2, N):
        ans = (num_1 + num_2) % 15746
        num_1 = num_2 
        num_2 = ans 

    print(ans)

# 메모리 초과 
# import sys 
# input = sys.stdin.readline 

# N = int(input())

# if N == 1:
#     print(1)
# else:
#     dp = [0] * N 
#     dp[0], dp[1] = 1, 2 

#     for i in range(2, N): 
#         dp[i] = dp[i-1] + dp[i-2]

#     print(dp[-1] % 15746)


# import sys 
# input = sys.stdin.readline 
# sys.setrecursionlimit(10**6)

# def find_tile(n, memo): 
#     if n == 1: 
#         return 1 
#     if n == 2:
#         return 2 
#     if memo.get(n):
#         return memo[n]
    
#     memo[n] = find_tile(n-1, memo) + find_tile(n-2, memo)

#     return memo[n]

# N = int(input())
# print(find_tile(N, {}) % 15746)
