class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]<nums[j]):
                    l.append(nums[j]-nums[i])
        if(len(l)>0):
            return max(l)
        else:
            return -1