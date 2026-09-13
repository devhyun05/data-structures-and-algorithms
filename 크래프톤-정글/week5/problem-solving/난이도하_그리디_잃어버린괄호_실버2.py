# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

equation = input()


equation_list = equation.split("-")
res = 0

for i in range(len(equation_list)): 
    curr_list = equation_list[i].split("+")

    for j in range(len(curr_list)):
        curr_list[j] = int(curr_list[j])

    num_sum = sum(curr_list)

    if i == 0:
        res += num_sum 
    else:
        res -= num_sum 

print(res)