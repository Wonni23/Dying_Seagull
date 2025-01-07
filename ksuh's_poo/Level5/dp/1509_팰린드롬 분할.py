st = input()
L = len(st)
dp = [i + 1 for i in range(L)] + [0]

for i in range(1, L):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    k = min(i, L - i - 1)
    left, right = i - 1, i + 1
    while right < i + k + 1:
        if st[left] != st[right]:
            break
        dp[right] = min(dp[right], dp[left - 1] + 1)
        right += 1
        left -= 1
    k = min(i - 1, L - i - 1)
    left, right = i - 1, i
    while right < i + k + 1:
        if st[left] != st[right]:
            break
        dp[right] = min(dp[right], dp[left - 1] + 1)
        right += 1
        left -= 1
print(dp[L - 1])

# TC

# BBCDDECAECBDABADDCEBACCCBDCAABDBADD
# 22

# AAAA
# 1

# ABCDEFGH
# 8

# QWERTYTREWQWERT
# 5