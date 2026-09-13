# DP - LCS (백준 9251)
# 앞에서부터 확인하는 Top-Down DP

import sys
sys.setrecursionlimit(10**6)

text1 = input()
text2 = input()

text1_length = len(text1)
text2_length = len(text2)

dp = [[-1] * text2_length for _ in range(text1_length)]

def longest_common_subsequence(text1_index, text2_index):
    # base case: 둘 중 하나라도 끝까지 가면 더 이상 공통 부분 수열이 없음
    if text1_index == text1_length or text2_index == text2_length:
        return 0

    if dp[text1_index][text2_index] != -1:
        return dp[text1_index][text2_index]

    # 현재 문자가 같은 경우
    if text1[text1_index] == text2[text2_index]:
        dp[text1_index][text2_index] = 1 + longest_common_subsequence(
            text1_index + 1, text2_index + 1
        )
    else:
        # 현재 문자가 다른 경우
        dp[text1_index][text2_index] = max(
            longest_common_subsequence(text1_index + 1, text2_index),
            longest_common_subsequence(text1_index, text2_index + 1)
        )

    return dp[text1_index][text2_index]

print(longest_common_subsequence(0, 0))