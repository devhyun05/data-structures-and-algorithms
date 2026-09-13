# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

# 시간 초과 
# nums = list(map(int, input().split()))

# base = nums[0]
# exponent = nums[1]
# moduler = nums[2]

# if exponent == 0:
#     print(1)

# num_to_multiply = base 

# if exponent > 0:            
#     for i in range(exponent-1):
#         base *= num_to_multiply 
# else: 
#     for i in range(abs(exponent)-1):
#         base *= num_to_multiply 
#     base = 1 / base

            
# print(base % moduler)


def fast_pow(base, exp, modular):
    if exp == 0:
        return 1

    half = fast_pow(base, exp // 2, modular)

    if exp % 2 == 0:
        return (half * half) % modular
    else:
        return (half * half * base) % modular

nums = list(map(int, input().split()))
base = nums[0]
exp = nums[1]
modular = nums[2]

print(fast_pow(base, exp, modular))

