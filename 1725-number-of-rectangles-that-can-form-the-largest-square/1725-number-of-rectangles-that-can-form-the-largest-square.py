from collections import defaultdict
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans=[]
        dic=defaultdict(int)
        for i in rectangles:
            dic[min(i)]+=1
        dict = sorted(dic.items(), key=lambda x: x[0],reverse=True)
        ans,farzi=dict[0]
        return farzi