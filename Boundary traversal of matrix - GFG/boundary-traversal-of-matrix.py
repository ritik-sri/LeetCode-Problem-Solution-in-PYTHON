class Solution:
    def BoundaryTraversal(self, matrix, n, m):
        ans = []
        # Base condition: if the matrix has only one element
        if n == 1 and m == 1:
            return [matrix[0][0]]
        
        # Boundary traversal logic
        for i in range(m):
            ans.append(matrix[0][i])
        for i in range(1, n):
            ans.append(matrix[i][-1])
        if n > 1:
            for i in range(m - 2, -1, -1):
                ans.append(matrix[n - 1][i])
        if m > 1:
            for i in range(n - 2, 0, -1):
                ans.append(matrix[i][0])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends