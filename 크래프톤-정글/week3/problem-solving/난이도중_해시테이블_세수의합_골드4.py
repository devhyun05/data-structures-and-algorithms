# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

# n = int(input())

# num_list = []
# num_map = {}

# for i in range(n):
#     num = int(input())
#     num_map[num] = i 
#     num_list.append(num)

# num_list.sort()
# max_sum = 0 
# n = len(num_list)
# target_pos = n - 1
# found_comb = False 

# while target_pos > 2: 
#     for i in range(target_pos):
#         for j in range(target_pos):
#             if num_list[target_pos] - (num_list[i] + num_list[j]) in num_map:
#                 print(num_list[target_pos])
#                 found_comb = True 
#                 break     
#     if found_comb:
#         break 

n = int(input())
num_list = []
num_map = {}

for i in range(n):
    num = int(input())
    num_list.append(num)

n = len(num_list)

for i in range(n):
    for j in range(n):
        comb = num_list[i] + num_list[j]
        num_map[comb] = 0

num_list.sort()
num_found = False 
for i in range(n-1, -1 ,-1):
    for j in range(i-1, -1, -1):
        print(f"num_list[j]: {num_list[j]}, num_list[i]: {num_list[i]}")
        comb = num_list[i] - num_list[j]
        if comb in num_map:
            print(num_list[i])
            num_found = True 
            break 
    if num_found:
        break 
        

    
    