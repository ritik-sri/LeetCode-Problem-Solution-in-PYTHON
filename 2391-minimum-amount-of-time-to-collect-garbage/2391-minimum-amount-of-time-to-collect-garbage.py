class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        first,second,third=0,0,0
        sumi=sum(travel)
        t1=0
        m,p,q=0,0,0
        res=0
        for i in range(len(garbage)):
            a=garbage[i].count('G')
            b=garbage[i].count('P')
            c=garbage[i].count('M')
            if a!=0:
                first+=(a+res-m)
                m=res
            if b!=0:
                second+=(b+res-p)
                p=res
            if c!=0:
                third+=(c+res-q)
                q=res
            if i<len(travel):
                res+=travel[i]
        return first+second+third