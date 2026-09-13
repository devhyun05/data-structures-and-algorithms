# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971


# 방법 1 순열: 

# permutation backtracking으로 구현 
# def permute(nums):  
#     res = []
#     remaining = nums[:]
#     def backtrack(curr_list, remaining):
#         if len(curr_list) == len(nums):
#             res.append(curr_list[:])
#             return
        
#         for i in range(len(remaining)): 
#             curr_list.append(remaining[i])

#             backtrack(curr_list, remaining[:i] + remaining[i+1:])
#             curr_list.pop()

#     backtrack([], remaining)
#     return res 

# num_of_cities = int(input())
# numbers = []
# cost_table = []

# for _ in range(num_of_cities): 
#     costs = list(map(int, input().split()))
#     cost_table.append(costs)

# for i in range(1, num_of_cities+1):
#     numbers.append(i)

# permute_nums = permute(numbers)

# min_score = float('inf')

# for i in range(len(permute_nums)):
#     curr_score = 0
#     possible = True

#     # 경로 내부 이동
#     for j in range(len(permute_nums[i]) - 1):
#         curr_city = permute_nums[i][j]
#         next_city = permute_nums[i][j + 1]
#         cost_table_val = cost_table[curr_city - 1][next_city - 1]

#         if cost_table_val == 0:
#             possible = False
#             break

#         curr_score += cost_table_val

#     # 마지막 도시 -> 시작 도시 복귀
#     if possible:
#         last_city = permute_nums[i][-1]
#         start_city = permute_nums[i][0]
#         return_cost = cost_table[last_city - 1][start_city - 1]

#         if return_cost == 0:
#             possible = False
#         else:
#             curr_score += return_cost

#     if possible:
#         min_score = min(min_score, curr_score)

# print(min_score)
# 방법 2 백트래킹: 
num_of_cities = int(input())
visited_cities = []

for _ in range(num_of_cities):
    visited_cities.append(list(map(int, input().split())))

visited = [False] * num_of_cities
answer = float('inf')

def backtrack(start_city, current_city, count, total_cost):
    global answer

    if count == num_of_cities:
        if visited_cities[current_city][start_city] != 0:
            answer = min(answer, total_cost + visited_cities[current_city][start_city])
        return

    for next_city in range(num_of_cities):
        if not visited[next_city] and visited_cities[current_city][next_city] != 0:
            visited[next_city] = True
            backtrack(start_city, next_city, count + 1, total_cost + visited_cities[current_city][next_city])
            visited[next_city] = False

for start in range(num_of_cities):
    visited[start] = True
    backtrack(start, start, 1, 0)
    visited[start] = False

print(answer)