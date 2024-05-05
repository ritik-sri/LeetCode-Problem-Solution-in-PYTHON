from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        prefsum=0
        count=0
        n=len(nums)
        for i in nums:
            prefsum+=i
            if prefsum-k in dic:
                count+=dic[prefsum-k]
            dic[prefsum]+=1
        return count 