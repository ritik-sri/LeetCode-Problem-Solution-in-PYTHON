
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        d[0]=1
        s=0
        ans=0
        for i in nums:
            s+=i
            ans+=d[s%k]
            d[s%k]+=1
        return ans
