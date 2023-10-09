class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posindex=0
        negindex=1
        res=[-1]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                res[posindex]=nums[i]
                posindex+=2
            else:
                res[negindex]=nums[i]
                negindex+=2
        return res