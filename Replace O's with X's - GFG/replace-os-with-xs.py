class Solution:
    def fill(self, n, m, mat):
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or vis[i][j] or mat[i][j] != 'O':
                return
            vis[i][j] = True
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        vis = [[False for _ in range(m)] for _ in range(n)]

        for j in range(m):
            if not vis[0][j] and mat[0][j] == 'O':
                dfs(0, j)
            if not vis[n - 1][j] and mat[n - 1][j] == 'O':
                dfs(n - 1, j)

        for i in range(n):
            if not vis[i][0] and mat[i][0] == 'O':
                dfs(i, 0)
            if not vis[i][m - 1] and mat[i][m - 1] == 'O':
                dfs(i, m - 1)

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O' and not vis[i][j]:
                    mat[i][j] = 'X'

        return mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends