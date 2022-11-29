class Solution:
    def rob(self, nums: List[int]) -> int:
        def maximum(nums,dp,i):
            if(i>=len(nums)):
                return 0
            if(dp[i]!=-1):
                return dp[i]
            left=nums[i]+maximum(nums,dp,i+2)
            right=maximum(nums,dp,i+1)
            dp[i]=max(left,right)
            return dp[i]
        dp=[-1]*len(nums)
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]
        else:
            maximum(nums,dp,0)
        return max(dp)