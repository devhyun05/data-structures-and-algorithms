# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

from collections import deque 

n, m = map(int, input().split())

miro = []

visited = set()

for i in range(n):
    map_status = list(map(int, input().strip()))
    miro.append(map_status)

map_width = m
map_height = n
depth = 1
queue = deque([(0,0,depth)])

while queue:
    x, y, depth = queue.popleft()

    if (x, y) == (map_height-1, map_width-1): 
        print(depth)
        break 

    # 위쪽 확인
    if (x-1) >= 0:
        if miro[x-1][y] != 0:
            if (x-1, y) not in visited:                
                queue.append((x-1, y, depth+1))
                visited.add((x-1, y))

    # 오른쪽 확인
    if (y+1) < map_width: 
        if miro[x][y+1] != 0:
            if (x, y+1) not in visited:
                queue.append((x, y+1, depth+1))
                visited.add((x, y+1))
    
    # 왼쪽 확인
    if (y-1) >= 0: 
        if miro[x][y-1] != 0:
            if (x, y-1) not in visited:
                queue.append((x, y-1, depth+1))
                visited.add((x, y-1))
  
    # 아래쪽 확인
    if (x+1) < map_height:
        if miro[x+1][y] != 0:
            if (x+1, y) not in visited:
                queue.append((x+1, y, depth+1))
                visited.add((x+1, y))
    
    