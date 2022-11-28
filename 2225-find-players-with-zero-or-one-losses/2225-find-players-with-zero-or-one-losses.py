from collections import OrderedDict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        od=OrderedDict()
        for i,j in matches:
            if j in od:
                od[j]+=1
            else:
                od[j]=1
        l=set()
        for i,j in matches:
            if i in od:
                pass
            else:
                l.add(i)
        m=[]
        for i,j in od.items():
            if j==1:
                m.append(i)
        s=[]
        s.extend([sorted(l)])
        s.extend([sorted(m)])
        return s
