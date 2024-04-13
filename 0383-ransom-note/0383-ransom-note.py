from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=Counter(ransomNote)
        b=Counter(magazine)
        for i in ransomNote:
            if i in magazine and b[i]>0:
                b[i]-=1
                if b[i]==0:
                    del b[i]
            else:
                return False
        return True
                