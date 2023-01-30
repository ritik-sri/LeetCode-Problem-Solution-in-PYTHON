from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m=[]
        l=[]
        dic=defaultdict(int)
        for i in arr1:
            if i in arr2:
                dic[i]+=1
            else:
                m.append(i)
        for i in arr2:
            for j in range(dic[i]):
                l.append(i)
        m.sort()
        return l+m
            