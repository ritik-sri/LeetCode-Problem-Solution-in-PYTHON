from collections import defaultdict
from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 2:
            return max(arr[0], arr[1])
        if k > len(arr):
            return max(arr)
        if arr[1]> arr[0] and k==1:
            return arr[1]
        winc = 0
        ans = arr[0]
        for i in range(1,len(arr)):
            if ans > arr[i]:
                winc += 1
                if winc == k:
                    return ans
            else:
                ans = arr[i]
                winc = 1
        return ans
