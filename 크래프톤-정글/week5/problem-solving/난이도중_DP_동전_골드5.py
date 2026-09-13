# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, M + 1):
            dp[j] += dp[j - coin]

    print(dp[M])



# n, k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]

# dp = [0] * (k + 1)
# dp[0] = 1

# for coin in coins:
#     for j in range(coin, k + 1):
#         dp[j] += dp[j - coin]

# print(dp[k])