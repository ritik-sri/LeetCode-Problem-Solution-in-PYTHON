from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        i = 0
        j = 0
        dic = defaultdict(int)
        while j < len(nums):
            dic[nums[j]] += 1
            if j - i + 1 <= len(dic):
                maxi = max(maxi, sum(nums[i:j+1]))
            while j - i + 1 > len(dic):
                dic[nums[i]] -= 1
                if dic[nums[i]] == 0:
                    del dic[nums[i]]
                i += 1
            j += 1
        return maxi
