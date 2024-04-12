class Solution:
    def finalString(self, s: str) -> str:
        l=[]
        out=""
        for i in s:
            if i=='i':
                out=""
                l=l[::-1]
                out="".join(l)
            else:
                l.append(i)
                out+=i
        return out