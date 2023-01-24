class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dfs(arr,i,j,dp):
            if j<0 or j>=len(arr[0]):
                return 1e9
            if i==0:
                return arr[0][j]
            if dp[i][j] != -1:
                return dp[i][j]
            up=dfs(arr,i-1,j,dp)+arr[i][j]

            left=dfs(arr,i-1,j-1,dp)+arr[i][j]

            right=dfs(arr,i-1,j+1,dp)+arr[i][j]

            dp[i][j]=min(up,left,right)
            return dp[i][j]
        dp=[[-1]*len(matrix[0]) for i in range(len(matrix))]
        mini=999999
        for i in range(len(matrix[0])):
            mini=min(mini,dfs(matrix,len(matrix)-1,i,dp))
        return mini