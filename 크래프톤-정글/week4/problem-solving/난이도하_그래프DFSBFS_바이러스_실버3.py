# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

from collections import deque 

vertices = int(input())
n = int(input())
graph = {}
queue = deque()
visited = set()

for i in range(1, vertices+1):
    graph[i] = []

for _ in range(n):
    start, end = map(int, input().split())
    graph[start].append(end)

queue.append(1)
count = 0

while queue: 
    curr_num = queue.popleft()
    if curr_num not in visited: 
        count += 1
        visited.add(curr_num)
        computers = graph[curr_num]

        for c in computers:    
            queue.append(c)

count -= 1
print(count)