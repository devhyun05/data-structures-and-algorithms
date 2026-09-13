# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

import sys 
input = sys.stdin.readline

from collections import deque 


n = int(input())
numbers = deque([i for i in range(1, n+1)])


while len(numbers) > 1: 
    numbers.popleft()
    numbers.append(numbers.popleft())

print(numbers[0])