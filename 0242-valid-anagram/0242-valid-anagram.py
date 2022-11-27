from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic=defaultdict(int)
        for i in s:
            dic[i]+=1
        for i in t:
            dic[i]-=1
            if dic[i]==0:
                del dic[i]
        if(len(dic)==0):
            return True
        else:
            return False
        