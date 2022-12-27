class Solution:
    def maximumBags(self, c: List[int], r: List[int], additionalRocks: int) -> int:
        a = []
        for i in range(len(c)):
            a.append(c[i]-r[i])
        a.sort()
        ans=0
        for i in a:
            if i==0:
                ans+=1
            elif i>additionalRocks:
                continue
            else:
                ans+=1
                additionalRocks-=i
        return ans
