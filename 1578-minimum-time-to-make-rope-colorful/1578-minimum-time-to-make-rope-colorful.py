class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time=0
        prevmax=0
        n=len(colors)
        for i in range(n):
            if(i>0 and colors[i]!=colors[i-1]):
                prevmax=0
            curr=neededTime[i]
            time+=min(prevmax,curr)
            prevmax=max(prevmax,curr)
        return time