# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

# # [
# #  [1,1,0,0,0,0,1,1]
# #  [1,1,0,0,0,0,1,1]
# #  [0,0,0,0,1,1,0,0]
# #  [0,0,0,0,1,1,0,0]
# #  [1,0,0,0,1,1,1,1]
# #  [0,1,0,0,1,1,1,1]
# #  [0,0,1,1,1,1,1,1]
# #  [0,0,1,1,1,1,1,1]
# # ]

n = int(input())
num_list = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    num_list.append(numbers)

res_white = 0
res_blue = 0

def find_paper(x, y, size):
    # 전역 스코프 변수 가져오기 
    global res_white 
    global res_blue 
    
    compare_with = num_list[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if num_list[i][j] != compare_with: 
                half = size // 2 
                find_paper(x, y, half) # 왼쪽 위 확인
                find_paper(x, y+half, half) # 오른쪽 위 확인 
                find_paper(x+half, y, half) # 왼쪽 아래 확인
                find_paper(x+half, y+half, half) # 오른쪽 아래 확인 
                return 
    
    if compare_with == 0:
        res_white += 1
    else:
        res_blue += 1
    
find_paper(0, 0, n)
print(res_white)
print(res_blue )




























