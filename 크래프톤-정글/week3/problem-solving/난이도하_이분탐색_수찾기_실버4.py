# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

# 풀이 1번: dictionary
# first_input = int(input())
# first_numbers = list(map(int, input().split()))
# num_map = {}

# for i in range(len(first_numbers)):
#     num_map[first_numbers[i]] = i 

# second_input = int(input())
# second_numbers = list(map(int, input().split()))

# for num in second_numbers:
#     if num in num_map:
#         print(1)
#     else:
#         print(0)

# 풀이 2번: hash set
# first_input = int(input())
# first_numbers = list(map(int, input().split()))
# num_set = set()

# for num in first_numbers: 
#     num_set.add(num)

# second_input = int(input())
# second_numbers = list(map(int, input().split()))

# for num in second_numbers:
#     if num in num_set: 
#         print(1)
#     else:
#         print(0)

# 풀이 3번: 이분 탐색 (binary search)
first_input = int(input())
first_numbers = list(map(int, input().split()))
first_numbers.sort()

second_input = int(input())
second_numbers = list(map(int, input().split()))

for num in second_numbers:
    start = 0
    end = len(first_numbers) - 1
    found_num = False

    while start <= end:
        mid = (start + end) // 2

        if first_numbers[mid] == num:
            found_num = True
            break
        elif first_numbers[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    if found_num:
        print(1)
    else:
        print(0)