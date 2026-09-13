# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

# 왼쪽에 낮은게 있으면 pop
# 왼쪽에 큰게 있으면 print
# 왼쪽에 더이상 없으면 0 

n = int(input())
nums = list(map(int, input().split()))

stack = []
ans = []

for i in range(len(nums)):
    if not stack:
        ans.append(0)
        stack.append((nums[i], i+1))
    else:
        if stack[-1][0] > nums[i]:
            ans.append(stack[-1][1])
            stack.append((nums[i], i+1))
        else:
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            if stack:
                ans.append(stack[-1][1])
                stack.append((nums[i], i+1))
            else:
                stack.append((nums[i], i+1))
                ans.append(0)


# for i in range(5):
#     print(i, end=' ')

for num in ans:
    print(num, end=' ')

