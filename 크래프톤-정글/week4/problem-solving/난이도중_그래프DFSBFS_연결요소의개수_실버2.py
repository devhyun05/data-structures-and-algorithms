# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (N + 1)
res = 0

for curr_num in range(1, N + 1):
    if not visited[curr_num]:
        queue = deque([curr_num])
        visited[curr_num] = True

        while queue:
            x = queue.popleft()

            for next_num in graph[x]:
                if not visited[next_num]:
                    visited[next_num] = True
                    queue.append(next_num)

        res += 1

print(res)