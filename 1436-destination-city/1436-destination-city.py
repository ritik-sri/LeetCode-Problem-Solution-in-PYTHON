from collections import defaultdict
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a = defaultdict(list)
        s = set()
        for i in paths:
            s.add(i[0])
            s.add(i[1])
            a[i[0]].append(i[1])
        p=a.keys()
        out=""
        for i in s:
            if i not in p:
                out=i
        return out
        
