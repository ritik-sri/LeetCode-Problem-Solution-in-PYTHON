from typing import List
import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        if len(dist) == 1 and len(speed) == 1:
            return 1
        
        l = [math.ceil(dist[i] / speed[i]) for i in range(len(dist))]
        l.sort()
        
        count = 0
        for i in range(len(l)):
            if l[i] <= i:
                return count
            count += 1
        
        return count
