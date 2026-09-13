# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

from collections import deque 

n, k = map(int, input().split())
coins = [] # [1,5,12]

dist = [-1] * (k + 1)
dist[0] = 0
for _ in range(n): 
    coins.append(int(input()))

# bfs 구현 
queue = deque([0])
ans = 0 

while queue: 
    curr_coin = queue.popleft()

    for coin in coins: 
        next_coin = curr_coin + coin 

        if next_coin < k:
            dist[next_coin] = dist[curr_coin] + 1  
            if dist[next_coin] == -1:
                queue.append(next_coin)
        elif next_coin == k: 
            ans = dist[curr_coin]
            break 

    
print(ans)


