from bisect import bisect_right
str1 = input()
str2 = input()

dp = [0] * len(str1)
d = [[] for _ in range(len(str1) + 1)]
d[0] = ["", -1]

for letter in str2:
    M = 0
    tmp = []
    for i in range(len(str1)):
        if str1[i] == letter:
            tmp.append(i)
        if dp[i] > M:
            M = dp[i]
            continue
        if str1[i] == letter:
            dp[i] = M + 1
    for i in range(M, -1, -1):
        st, idx = d[i]
        result = bisect_right(tmp, idx)
        if result < len(tmp) and (not d[i + 1] or d[i + 1][1] > tmp[result]):
            d[i + 1] = [st + letter, tmp[result]]

M = max(dp)
print(M)
if M:
    print(d[M][0])


a = ' '+input()
b = ' '+input()
al, bl = len(a)-1, len(b)-1

dp = [[0]*(bl+1) for _ in range(al+1)]

for i in range(1,al+1):
    for j in range(1,bl+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
ans = ''
K = dp[-1][-1]
while K > 0:
    if al == 0 or bl == 0:
        break;
    if a[al] == b[bl]:
        ans = a[al]+ans
        al, bl = al-1, bl-1
        K -= 1
    else:
        if dp[al-1][bl] >= dp[al][bl-1]: al -= 1
        else: bl -= 1

print(dp[-1][-1])
print(ans)



# C
# C CA A
# C CA CAP AP A
# C CA CAP AP A AC
# C CA CAP AP A AC ACA
# CAK CAP A AC ACK ACA ACAK

# TC
#
# ACAYKP
# CAPCAK
#
# 4
# ACAK

# ABCDEF
# BEFDEFACDFABZ

# KKKBCBCAAA
# KCKBCBCAKK

# 7
# KKBCBCA

# ADQWEQWDQWGFSDAHWREYERFGD
# FGDGFDSGWERDSAFLSD
# ADEDFSDFD

# ASDWADGFRQWE
# GHASDQWEZZZZZ