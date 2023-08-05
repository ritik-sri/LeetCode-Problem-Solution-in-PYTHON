class Solution:

    def findMinDiff(self, A, N, M):
        A = sorted(A)
        i = 0
        mini = float("inf")

        while i <= N - M: 
            c = A[i + M - 1] - A[i]
            mini = min(mini, c)
            i += 1

        return mini




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends