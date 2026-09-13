# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

n = int(input())

text_map = {}

for _ in range(n):
    pwd = input()
    if pwd == pwd[::-1] or pwd in text_map:
        print(f"{len(pwd)} {pwd[len(pwd) // 2]}")
    else: 
        text_map[pwd[::-1]] = 0
       