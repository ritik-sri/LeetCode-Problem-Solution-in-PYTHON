class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a=sum(nums)
        numi=""
        for i in nums:
            numi+=str(i)
        numi=int(numi)
        sumi=0
        while numi>0:
            sumi+=numi%10
            numi//=10
        b=int(sumi)
        return abs(a-b)