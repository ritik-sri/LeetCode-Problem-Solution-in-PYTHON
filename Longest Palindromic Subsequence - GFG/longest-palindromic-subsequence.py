#User function Template for python3
def lcs(X, Y, m, n, dp):
    if (m == 0 or n == 0):
        return 0
    if (dp[m][n] != -1):
        return dp[m][n]
    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
        return dp[m][n]
    else:
        dp[m][n] = max(lcs(X, Y, m, n - 1, dp),lcs(X, Y, m - 1, n, dp))
        return dp[m][n]

class Solution:
    

    def longestPalinSubseq(self, S):
        # code here
        s2 = S
        s2 = s2[::-1]
        n=len(S)
        dp = [[-1 for i in range(n+1)] for i in range(n+1)]
        return lcs(s2,S,n,n,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends