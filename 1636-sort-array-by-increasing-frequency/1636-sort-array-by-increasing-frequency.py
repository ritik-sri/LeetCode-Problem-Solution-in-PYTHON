
        
from collections import defaultdict
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        a = sorted(dic.items(), key=lambda item: item[1])
        b = max(dic.values())
        my_dict = {i: [] for i in range(1,b+1)}
        for i, j in dic.items():
            my_dict[j].append(i)
        ans=[]
        for i,j in my_dict.items():
            k=j
            if len(k)>1:
                k=sorted(k)[::-1]
            for p in k:
                ans.extend(i*[p])
        return ans