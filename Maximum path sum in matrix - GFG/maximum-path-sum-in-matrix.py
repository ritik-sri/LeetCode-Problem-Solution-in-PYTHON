#User function Template for python3

class Solution:
    def maximumPath(self, N, matrix):
        # code here
        n, m = len(matrix), len(matrix[0])
        dp = [[-1] * m for _ in range(n)]
        
        def f(i, j):
            if j < 0 or j >= m:
                return -1e9
            if i == 0:
                return matrix[0][j]
            if dp[i][j] != -1:
                return dp[i][j]           
            s = matrix[i][j] + f(i-1, j)
            l = matrix[i][j] + f(i-1, j-1)
            r = matrix[i][j] + f(i-1, j+1)
            dp[i][j] = max(max(s, l), r)
            return dp[i][j]
        
        ans = -1e9
        for j in range(m):
            ans = max(ans, f(n-1, j))
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends