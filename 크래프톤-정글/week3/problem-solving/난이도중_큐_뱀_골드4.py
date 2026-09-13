# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque 

board_size = int(input())
board = [[0]*board_size for _ in range(board_size)]

num_of_apples = int(input())
for _ in range(num_of_apples):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

command_count = int(input())
queue = deque()
for _ in range(command_count):
    s, cmd = input().split()
    queue.append((int(s), cmd))

snake = deque()
snake.append((0,0))

direction = 0  # 0:오른쪽, 1:아래, 2:왼쪽, 3:위
dx = [0,1,0,-1]
dy = [1,0,-1,0]

time = 0

while True:
    time += 1

    head_x, head_y = snake[-1]
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    # 벽
    if nx < 0 or nx >= board_size or ny < 0 or ny >= board_size:
        break

    # 자기 몸
    if (nx, ny) in snake:
        break

    snake.append((nx, ny))

    # 사과 있으면 안 줄임
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        snake.popleft()

    # 방향 전환
    if queue and queue[0][0] == time:
        _, cmd = queue.popleft()
        if cmd == 'L':
            direction -= 1
        else:
            direction += 1
        direction %= 4

print(time)

