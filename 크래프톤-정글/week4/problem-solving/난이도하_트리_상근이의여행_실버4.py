# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

from collections import deque

T = int(input())

for i in range(T): 
    n, m = list(map(int, input().split()))
    vertices = [i+1 for i in range(n)]
    graph  = {}
    edges = []
    queue = deque()
    visited = set()
    
    for v in vertices: 
        graph[v] = []

    for _ in range(m):
        start, end = list(map(int, input().split()))
        edges.append((start, end))
 
    for e in edges: 
        start, end = e   
        graph[start].append(end)   
        graph[end].append(start)   

    start_item = graph[1]

    for item in start_item:
        queue.append(item)

    distance = 0

    while queue:
        curr_num = queue.popleft()
        if curr_num not in visited: 
            visited.add(curr_num)
            distance += 1 

            next_dest = graph[curr_num]

            if next_dest:
                for dest in next_dest:
                    queue.append(dest)
                
    distance -= 1
    print(distance)
 

    