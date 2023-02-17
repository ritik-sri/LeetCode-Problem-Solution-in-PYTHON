def lps(X, Y, m, n, dp):
    if (m == 0 or n == 0):
        return 0
    if (dp[m][n] != -1):
        return dp[m][n]
    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lps(X, Y, m - 1, n - 1, dp)
        return dp[m][n]
    else:
        dp[m][n] = max(lps(X, Y, m, n - 1, dp),lps(X, Y, m - 1, n, dp))
        return dp[m][n]
    
class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[-1 for i in range(len(s)+1)] for i in range(len(s)+1)]
        a=lps(s,s[::-1],len(s),len(s),dp)
        return len(s)-a
        
        
        