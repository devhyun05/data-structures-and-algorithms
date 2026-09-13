# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys 
input = sys.stdin.readline 

N, K = map(int, input().split())
coins = []

for _ in range(N): 
    coins.append(int(input()))

coins = coins[::-1]
coin_count = 0 
curr_sum = 0 

for coin in coins: 
    curr_count = K // coin 
    if curr_count >= 1: 
        K -= (coin * curr_count) 
        coin_count += curr_count 
    if K == 0: 
        print(coin_count)
        break 
