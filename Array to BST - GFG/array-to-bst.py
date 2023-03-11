class Solution:
    def sortedArrayToBST(self, nums):
        low=0
        high=len(nums)-1
        ans=[]
        def ToBst(nums, ans, low, high):
            if low>high:
                return
            mid=(low+high)//2
            ans.append(nums[mid])
            ToBst(nums,ans, low, mid-1)
            ToBst(nums,ans, mid+1, high)
        ToBst(nums, ans, low, high)
        return ans

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends