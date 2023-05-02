#User function Template for python3

class Solution:
    def countZeroes(self, A, N):
        n=len(A)
        m=len(A[0])
        i=0
        j=m-1
        count=0
        while(i>=0 and i<m and j>=0 and j<n):
            if(A[i][j]==1):
                j-=1
            else:
                count+=(j+1)
                i+=1
        return count

#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n)]for j in range(n)]
        k=0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[k]
                k+=1
        
        ob = Solution()
        print (ob.countZeroes(matrix, n))
        
# } Driver Code Ends