class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n):
            l,h = 0,i - 1
            while l <= h:
                mid = (l + h) >> 1
                if nums[mid] + nums[i] >= lower:
                    h = mid - 1
                else:
                    l = mid + 1
            ind = h + 1
            l,h = ind,i - 1
            while l <= h:
                mid = (l + h) >> 1
                if nums[mid] + nums[i] <= upper:
                    l = mid + 1
                else:
                    h = mid - 1
            ans += (l - ind)
        return ans