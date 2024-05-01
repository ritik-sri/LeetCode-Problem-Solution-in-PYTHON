from collections import Counter
import math
from typing import List
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        dic=defaultdict(list)
        for i,j in enumerate(nums):
            if is_prime(j):
                dic[j].append(i)
        final=[]
        for i,j in dic.items():
            final.extend(j)
        if len(final)>1:
            return max(final)-min(final)
        else:
            return 0
