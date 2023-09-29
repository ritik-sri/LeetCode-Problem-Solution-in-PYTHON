from typing import List

class Solution:
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        stack = []
        
        # Mark boundary '1's as visited and push them to the stack
        for i in range(n):
            if grid[i][0] == 1:
                stack.append((i, 0))
            if grid[i][m - 1] == 1:
                stack.append((i, m - 1))
        for j in range(m):
            if grid[0][j] == 1:
                stack.append((0, j))
            if grid[n - 1][j] == 1:
                stack.append((n - 1, j))
        
        # Perform DFS using the stack
        while stack:
            i, j = stack.pop()
            if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                grid[i][j] = 0  # Mark cell as visited
                # Explore neighbors
                stack.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
        
        # Count remaining '1's (enclaves) after DFS
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        
        return count


    
    
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