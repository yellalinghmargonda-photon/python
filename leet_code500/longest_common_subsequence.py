def LCS(i, j,word1, word2):
    if i==len(word1) and j ==len(word2):
        return 0
    if word1[i]==word2[j]:
        return 1+LCS(i+1, j+1, word1, word2)
    return max(LCS(i + 1, j, word1, word2),LCS(i + 1, j, word1, word2))


def LCSDP(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if word1[i] == word2[j]:  # Fix: Compare word1[i] with word2[j]
                dp[i][j] = 1 + dp[i + 1][j + 1]  # Fix: Correct LCS formula
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]  # Returns the LCS length
print(LCSDP("abcde", "ace"))  # Output: 3 (LCS = "ace")
print(LCSDP("abc", "def"))    # Output: 0 (No common subsequence)
print(LCSDP("aggtab", "gxtxayb"))  # Output: 4 (LCS = "gtab")



