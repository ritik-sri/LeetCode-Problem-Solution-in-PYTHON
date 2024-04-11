from collections import Counter
from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            p_to_w = {}  # Mapping from pattern character to word character
            w_to_p = {}  # Mapping from word character to pattern character
            
            for p_char, w_char in zip(pattern, word):
                if p_char not in p_to_w:
                    p_to_w[p_char] = w_char
                if w_char not in w_to_p:
                    w_to_p[w_char] = p_char
                if p_to_w[p_char] != w_char or w_to_p[w_char] != p_char:
                    return False
            return True
        
        ans = []
        for word in words:
            if match(word):
                ans.append(word)
        return ans

