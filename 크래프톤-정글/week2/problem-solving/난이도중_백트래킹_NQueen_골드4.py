# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

# 동작은 하지만 백준에서 pass
n = int(input())

# queen을 겹치지 않게 놓을 수 있는 경우의 수 카운트 
count = 0

# 현재 퀸이 어디에 있는지 알려주는 배열 
# queen[0] = 2라면 0번째 행의 2번째 열에 퀸이 있다는 것 
queen = [0] * n

def check_queen(row):
    global count

    # 퀸 n개만큼 전부 놓았을때 
    if row == n:
        count += 1
        return

    for col in range(n):
        can_place = True

        for i in range(row):            
            # 같은 열에 이미 퀸이 있는지 확인하는 코드 
            if queen[i] == col:
                can_place = False
                break
            
            # 대각선 확인하는 코드 
            if abs(row - i) == abs(col - queen[i]): 
                can_place = False  
                break
        
        # 현재 행에 퀸을 놓을 수 있다면
        # 현재 행에 놓고 다음 행에 퀸을 놓을 수 있는지 재귀적으로 탐색 
        if can_place:
            queen[row] = col
            check_queen(row + 1)

check_queen(0)
print(count)