from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1] * (i + 1) for i in range(n)]

        def dfs(i, j):
            if i == n - 1:
                return triangle[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = dfs(i + 1, j)
            right = dfs(i + 1, j + 1)
            
            dp[i][j] = triangle[i][j] + min(up, right)
            return dp[i][j]

        return dfs(0, 0)
