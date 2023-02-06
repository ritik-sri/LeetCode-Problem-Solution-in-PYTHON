class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            a=str(i)
            for j in a:
                l.append(int(j))
        return l