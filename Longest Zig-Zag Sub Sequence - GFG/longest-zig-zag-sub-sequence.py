class Solution:
    def ZigZagMaxLength(self, nums):
        inc=1
        dec=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc=dec+1
            elif nums[i]<nums[i-1]:
                dec=inc+1
        return max(inc,dec) 
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.ZigZagMaxLength(A))
# } Driver Code Ends