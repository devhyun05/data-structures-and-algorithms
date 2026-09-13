# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020


# 기초 10번에서 가져온 함수입니다 
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


test_case_count = int(input())

for _ in range(test_case_count):
    even_number = int(input())
    
    # 예시: 8이라면 4부터 시작해서 처음 나온 숫자가 가장 작은 소수의 합 
    left_prime_candidate = even_number // 2
    
    while left_prime_candidate > 1:
        right_prime_candidate = even_number - left_prime_candidate
        
        if is_prime(left_prime_candidate) and is_prime(right_prime_candidate):
            print(left_prime_candidate, right_prime_candidate)
            break

        left_prime_candidate -= 1