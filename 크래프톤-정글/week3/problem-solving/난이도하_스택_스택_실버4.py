# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys 
input = sys.stdin.readline

stack = []

n = int(input())

for _ in range(n):
    items = input().strip().split()   
    action = items[0]

    if len(items) > 1:         
        number = int(items[1])
        stack.append(number)
    else:
        if action == "push":
            stack.append(int(items[1][0]))
        if action == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif action == "size":
            print(len(stack))
        elif action == "empty":
            if len(stack) == 0: 
                print(1)
            else:
                print(0)
        elif action == "pop":
            if stack: 
                print(stack.pop())
            else:
                print(-1)

    


