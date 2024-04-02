from typing import List
from collections import defaultdict

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxi = 0
        idx = defaultdict(list)
        for i, row in enumerate(mat):
            count_ones = row.count(1)
            if count_ones >= maxi:
                maxi = count_ones
                idx[maxi].append(i)
        sorted_dict = (dict(sorted(idx.items(), reverse=True)))
        first_key, first_value = next(iter(sorted_dict.items()))
        l=[]
        l.append(min(first_value))
        l.append(first_key)
        return l