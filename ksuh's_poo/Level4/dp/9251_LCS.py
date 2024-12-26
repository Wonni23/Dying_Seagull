# 다이나믹 프로그래밍
# 문자열

# [0 0 0 0 0 0]
# C [0 1 0 0 0 0]
# A [1 1 2 0 0 0]
# P [1 1 2 0 0 3]
# C [1 2 2 0 0 3]
# A [1 2 3 0 0 3]
# K [1 2 3 0 4 3]

str1 = input()
str2 = input()

dp = [0] * len(str1)
for letter in str2:
    M = 0
    for idx in range(len(str1)):
        if M < dp[idx]:
            M = dp[idx]
            continue
        if str1[idx] == letter:
            dp[idx] = M + 1
print(max(dp))

# TC
# ACAYKP
# CAPCAK
#
# 4