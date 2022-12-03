from heapq import *
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i] , 0)  + 1
        maxHeap = [[-freq, val] for val, freq in dic.items()]
        heapq.heapify(maxHeap)
        out=""
        #print(maxHeap)
        while maxHeap:
            val,char=heapq.heappop(maxHeap)
            out+=abs(val)*char
        return out