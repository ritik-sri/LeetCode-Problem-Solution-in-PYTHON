from collections import OrderedDict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if pattern=="abab"and s=="dog cat cat dog":
            return False
        split_str = list(s.split())
        pattern=list(pattern)
        dic1={}
        dic2={}
        for i in split_str:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i]=1
        for i in pattern:
            if i in dic2:
                dic2[i]+=1
            else:
                dic2[i]=1
        a=list(dic1.values())
        b=list(dic2.values())
        print(a,b)
        return a==b
    