from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)-3+1):
            a=s[i:i+3]
            if len(set(a))==3:
                ans+=1
        return ans
            