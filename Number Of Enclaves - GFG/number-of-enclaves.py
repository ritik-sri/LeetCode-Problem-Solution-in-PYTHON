#User function Template for python3
from typing import List
from collections import deque
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        q = deque()
        m = len(grid[0])
        n = len(grid)
        vis = [[0] * m for _ in range(n)]  

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    if grid[i][j] == 1:  
                        q.append((i, j)) 
                        vis[i][j] = 1

        delrow = [-1, 0, 1, 0] 
        delcol = [0, 1, 0, -1]  

        while q:
            a = q.popleft()
            row = a[0]
            col = a[1]
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if (nrow>0 and nrow<n) and (ncol>=0 and ncol<m):  
                    if vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                        q.append((nrow, ncol))
                        vis[nrow][ncol] = 1

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0: 
                    cnt += 1
        return cnt
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends