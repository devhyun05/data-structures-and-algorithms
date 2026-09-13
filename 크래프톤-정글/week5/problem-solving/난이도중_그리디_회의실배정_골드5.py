# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys 
input = sys.stdin.readline 

N = int(input())
meetings = []

for _ in range(N): 
    start, end = map(int, input().split())    
    meetings.append((start, end))

meetings.sort()


curr_meeting = meetings[0]
res = 0 

for i in range(1, len(meetings)):
    if meetings[i][0] >= curr_meeting[1]:    
        res += 1
        curr_meeting = meetings[i]
    elif meetings[i][1] < curr_meeting[1]:
        curr_meeting = meetings[i]
    

print(res+1)