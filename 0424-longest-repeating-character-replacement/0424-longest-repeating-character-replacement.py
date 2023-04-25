from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        maxi=0
        dic=defaultdict(int)
        while j<len(s):
            dic[s[j]]+=1
            if (j-i+1)-max(dic.values())<=k:
                pass
                maxi=max(maxi,j-i+1)
            else:
                while(((j-i+1)-max(dic.values()))>k):
                    dic[s[i]]-=1
                    if dic[s[i]]==0:
                        del dic[s[i]]
                    i+=1
            j+=1
        return maxi