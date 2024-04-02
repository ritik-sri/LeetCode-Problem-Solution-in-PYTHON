from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sumi=0
        a=Counter(nums)
        for i,j in a.items():
            if j==1:
                sumi+=i
        return sumi