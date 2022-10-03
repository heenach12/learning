def interleaving_string(s1, s2, s3):
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            choose_s1, choose_s2 = False, False
            if s1[i - 1] == s3[i + j - 1]:
                choose_s1 = dp[i - 1][j]
            if s2[j - 1] == s3[i + j - 1]:
                choose_s2 = dp[i][j - 1]
            dp[i][j] = choose_s1 or choose_s2

    return dp[m][n]



s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

d = interleaving_string(s1, s2, s3)
print("d is", d)

def dfs(i, j):
    if i == len(s1) and j == len(s2):
        return True
    choose_s1, choose_s2 = False, False
    if i < len(s1) and s1[i] == s3[i + j]:
        choose_s1 = dfs(i + 1, j)
    if j < len(s2) and s2[j] == s3[i + j]:
        choose_s2 = dfs(i, j + 1)

    return choose_s1 or choose_s2
# return dfs(0, 0)

