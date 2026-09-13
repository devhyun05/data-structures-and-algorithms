# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# s = input()
# word_dict = {}

# for c in s.lower():
#     word_dict[c] = word_dict.get(c, 0) + 1
    
# max_count = 0

# for c, char_count in word_dict.items():
#     if char_count > max_count: 
#         max_count = char_count 

# occur_times = 0
# ans = ""

# for c, char_count in word_dict.items():
#     if char_count == max_count: 
#         occur_times += 1
#         ans = c.upper()

# if occur_times > 1: 
#     print("?")
# else:
#     print(ans)
    

# 다시 풀어보기 

# 알파벳의 개수를 카운트해야 한다 
# dict를 사용하며 각 알파벳을 카운트한다 
# 중요한건 알파벳을 먼저 소문자로 바꿔야 한다
# 효율성을 위해서 알파벳을 추가하면서 뭐가 많은지도 같이 카운트한다 
word = input()
word_count_dict = {}
max_occ = float("-inf")

for c in word.lower(): 
    word_count_dict[c] = word_count_dict.get(c, 0) + 1 

    if word_count_dict.get(c) > max_occ: 
        max_occ = word_count_dict.get(c)

max_occ_char = []
for c, char_count in word_count_dict.items():
    if char_count == max_occ: 
        max_occ_char.append(c) 

# 개수가 가장 많은걸 확인하고 1개 이상 일때는 ?, 이하일때는 그 알파벳을 출력한다 
if len(max_occ_char) > 1: 
    print("?")
else:
    print(max_occ_char[0].upper())