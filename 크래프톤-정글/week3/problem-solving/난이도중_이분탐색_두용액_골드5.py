# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

# [-99, -2, -1, 4, 98]

# n = int(input())
# nums = list(map(int, input().split()))
# nums.sort()


# min_num = nums[0]

# for i in range(len(nums)):
#     left = 0
#     right = len(nums) - 1
#     curr_sum = 0
    
#     while left < right: 
#         mid = (left + right) // 2
#         curr_sum = nums[i] + nums[mid]u

# 투포인터 방법 
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
p1 = 0
p2 = len(nums)-1 
closest_to_zero = float("inf")
ans1, ans2 = 0, 0

while p1 < p2: 
    num_sum = nums[p1] + nums[p2]
    
    if abs(num_sum) < closest_to_zero:
        ans1, ans2 = nums[p1], nums[p2]
        closest_to_zero = abs(num_sum)
    
    if num_sum < 0: 
        p1 += 1 
    else:
        p2 -= 1 

print(ans1, ans2)

    
    

    