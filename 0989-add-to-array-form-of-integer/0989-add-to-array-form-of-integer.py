class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        out=""
        for i in num:
            out+=str(i)
        out=int(out)
        c=out+k
        c=str(c)
        ans=[]
        for i in c:
            ans.append(int(i))
        return ans