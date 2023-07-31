class Solution:

    def shortestCommonSupersequence(self, X, Y, m, n):
        def lcs(s1, s2, m, n, dp):
            if m == 0 or n == 0:
                return 0
            if dp[m - 1][n - 1] != -1:
                return dp[m - 1][n - 1]
            if s1[m - 1] == s2[n - 1]:
                dp[m - 1][n - 1] = 1 + lcs(s1, s2, m - 1, n - 1, dp)
            else:
                dp[m - 1][n - 1] = max(lcs(s1, s2, m - 1, n, dp), lcs(s1, s2, m, n - 1, dp))
            return dp[m - 1][n - 1]

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        lcs_length = lcs(X, Y, m, n, dp)
        return (m + n) - lcs_length
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends