# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

plate = int(input())

def hanoi_tower(n, fr, mid, to):
    if n == 0:
        return 
    
    hanoi_tower(n-1, fr, to, mid)
    print(fr, to)
    hanoi_tower(n-1, mid, fr, to)

print(2**plate-1)
hanoi_tower(plate, 1, 2, 3)