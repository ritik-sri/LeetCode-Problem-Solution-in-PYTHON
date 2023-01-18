class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        ans = nums[0]
        s = 0
        for i in nums:
            s += i
            ans = max(ans, s)
            if s <= 0:
                s = 0
        
        pref = [0 for i in range(len(nums))]
        suf = [0 for i in range(len(nums))]
        pref[0] = nums[0]
        suf[-1] = nums[-1]
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + nums[i]
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] + nums[i]
        for i in range(1, len(nums)):
            pref[i] = max(pref[i], pref[i-1])
        for i in range(len(nums)-2, 0, -1):
            suf[i] = max(suf[i], suf[i+1])
            
        for i in range(len(nums)):
            l = pref[i]
            r = 0
            if i+1 < len(nums):
                r = suf[i+1]
            ans = max(ans, l+r)
      

        return ans