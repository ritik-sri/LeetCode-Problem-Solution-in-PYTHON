import heapq
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        p=len(tasks)//len(processorTime)
        tasks=sorted(tasks)
        l=[]
        processorTime.sort()
        for j in processorTime:
            maxi=float("-inf")
            for i in range(p):
                a=tasks.pop()
                maxi=max(maxi,j+a)
            l.append(maxi)
        if len(l)>0:
            return max(l)
        