# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# import sys
# input = sys.stdin.readline

# n = int(input())

# for _ in range(n):
#     student_data = list(map(int, input().split()))
#     total_student = student_data[0]
#     grade_avg = sum(student_data[1:]) / total_student 
    
#     student_over_avg = 0 
    
#     for i in range(1, len(student_data)):
#         if student_data[i] > grade_avg: 
#             student_over_avg += 1 
    
#     result = (student_over_avg / total_student) * 100
#     print(f"{result:.3f}%")

# 테스트 케이스의 개수 
c = int(input())

for _ in range(c): 
    student_info = list(map(int, input().split()))
    grade_avg = sum(student_info[1:]) / student_info[0]
    count = 0
    
    for i in range(1, len(student_info)):
        if student_info[i] > grade_avg: 
            count += 1
            
    print(f"{(count / student_info[0]) * 100:.3f}%")
    
 