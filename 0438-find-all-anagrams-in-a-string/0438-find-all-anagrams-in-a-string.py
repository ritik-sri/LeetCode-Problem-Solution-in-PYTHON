class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic1={}
        for i in p:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i]=1
        i=0
        j=len(p)-1
        l=[]
        dic2=Counter(s[i:j])
        while(j<len(s)):
            dic2[s[j]]+=1
            if(dic1==dic2):
                l.append(i)
            dic2[s[i]]-=1
            if(dic2[s[i]])==0:
                del dic2[s[i]]
            i+=1
            j+=1
        return l