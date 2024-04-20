from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        if set(c1.keys()) != set(c2.keys()):
            return False
        
        a = sorted(c1.values())
        b = sorted(c2.values())
        if a==b:
            return True
        else:
            return False
