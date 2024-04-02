class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if nums:
            nums.remove(min(nums))
        else:
            return -1
        if nums:
            nums.remove(max(nums))
        else:
            return -1
        return nums[0] if nums else -1