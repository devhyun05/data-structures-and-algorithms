# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

from collections import deque 
import sys 
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

queue = deque()
queue.append(1)
parent = [0] * (n+1)
visited = [False] * (n+1)

visited[1] = True # 미리 추가해야 한다, 1도 방문을 했기 때문에 

while queue: 
    
    curr_num = queue.popleft() # 1 
  
    for i in graph[curr_num]:
        if not visited[i]: 
            parent[i] = curr_num 
            visited[curr_num] = True 
            queue.append(i)


for i in range(2, n+1):
    print(parent[i])
