#User function Template for python3
class Solution:
	def findMaxSum(self,arr, n):
	    dp=[-1]*(n+1)
	    dp[0]=arr[0]
	    for idx in range(1,n):
	        left=arr[idx]
	        if idx>1:
	            left+=dp[idx-2]
	        right=0+dp[idx-1]
	        dp[idx]=max(left,right)
	    return dp[n-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends