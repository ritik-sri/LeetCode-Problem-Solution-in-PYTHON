class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        low=len(nums)-1
        cnt=0
        high=len(nums)-1
        n = len(nums)
        i=0
        while(i<high):
            low=max(i,low)
            while(low>i and nums[i]+nums[low]>=lower):
                low-=1
            while(high>low and nums[i]+nums[high]>upper):
                high-=1
            cnt+=high-low
            i+=1
        return cnt
            
            