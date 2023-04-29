#User function Template for python3
class Solution:
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,matrix, n):
        n = len(matrix)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[j][n-i-1] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[n-i-1][n-j-1] = ans[i][j]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends