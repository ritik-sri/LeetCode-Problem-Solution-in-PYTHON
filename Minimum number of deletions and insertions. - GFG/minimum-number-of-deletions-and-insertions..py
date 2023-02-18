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
	def minOperations(self, s1, s2):
        m = len(s1)
        n = len(s2)
        dp = [[-1 for i in range(n+1)] for i in range(m+1)]
        a=m-lcs(s1,s2,m,n,dp)
        b=abs(lcs(s1,s2,m,n,dp)-n)
        return a+b
        
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends