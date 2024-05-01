from collections import defaultdict
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        dic = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                p = nums[i:j+1]
                dic.append(tuple(p))
        res=[]
        for i in dic:
            res.append(len(set(i))**2)
        return sum(res)