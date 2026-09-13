# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = map(int, input().split())

# 리프 수 만큼 생성
for i in range(1, m + 1):
    print(0, i)

# 마지막 리프에 이어 붙이기 
for i in range(m + 1, n):
    print(i - 1, i)