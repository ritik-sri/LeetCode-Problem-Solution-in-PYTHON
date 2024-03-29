class Solution:
    def rowWithMax1s(self, arr, n, m):
        ans = -1  # Initialize with -1 instead of 0
        maxi = 0  # Initialize with 0 instead of float("-inf")

        for i, j in enumerate(arr):
            count_ones = j.count(1)
            if count_ones > maxi:
                maxi = count_ones
                ans = i

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends