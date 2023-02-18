def lcs(X, Y, m, n, dp):
    if m == 0 or n == 0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
        return dp[m][n]
    else:
        dp[m][n] = max(lcs(X, Y, m, n - 1, dp), lcs(X, Y, m - 1, n, dp))
        return dp[m][n]


class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m = len(s1)
        n = len(s2)
        dp = [[-1 for j in range(n + 1)] for i in range(m + 1)]
        a = lcs(s1, s2, m, n, dp)
        i = m
        j = n
        scs = ""
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                scs += s1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                    scs += s1[i]
                else:
                    j -= 1
                    scs += s2[j]
        while i > 0:
            scs += s1[i-1]
            i -= 1
        while j > 0:
            scs += s2[j-1]
            j -= 1
        return scs[::-1]
