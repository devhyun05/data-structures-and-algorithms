# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys 
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    scores = []
    res = 0 

    for _ in range(N):
        document_score, interview_score = map(int, input().split())
        scores.append((document_score, interview_score))

    scores.sort()
    curr_score = scores[0][1]

    for i in range(1, len(scores)):
        if scores[i][1] < curr_score: 
            res += 1 
            curr_score = scores[i][1]
    
    print(res + 1)



