class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums=sorted(nums)
        count=0
        steps=0
        while(len(set(nums))!=len(nums)):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    temp = abs(nums[i] - nums[i-1]) + 1
                    nums[i] += temp 
                    steps += temp
        return steps 