# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import deque 

N, M, V = map(int, input().split())
graph = {}
queue = deque([V])
res = []
bfs_visited = set()
bfs_visited.add(V)

for i in range(N):
    graph[i+1] = []

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in graph:
    graph[i].sort()

while queue:
    
    curr_num = queue.popleft()
    res.append(curr_num)

    next_nums = graph[curr_num]

    for num in next_nums:
        if num not in bfs_visited: 
            bfs_visited.add(num)
            queue.append(num)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    
    visited.append(start)

    for num in graph[start]:
        if num not in visited: 
            dfs(graph, num, visited)
    
    return visited 

print(*dfs(graph, V))
print(*res)