# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

from collections import deque 

n = int(input())
board = []

for _ in range(n):
    num_list = list(map(int, input().split()))
    board.append(num_list)

queue = deque()
queue.append((0, 0))
board_size = len(board)
answer_found = False 
visited = set()

while queue: 
    x, y = queue.popleft()
    curr_num = board[x][y]
    next_x, next_y = x + curr_num, y + curr_num


    if next_y < board_size:
        if board[x][next_y] == -1:
            answer_found = True 
            break 
        else:
            if (x, next_y) not in visited:
                visited.add((x, next_y))
                queue.append((x, next_y))
                

    if next_x < board_size: 
        if board[next_x][y] == -1:
            answer_found = True 
            break 
        else:
            if (next_x, y) not in visited:
                visited.add((next_x, y))
                queue.append((next_x, y))        

if answer_found:
    print("HaruHaru")
else:
    print("Hing")