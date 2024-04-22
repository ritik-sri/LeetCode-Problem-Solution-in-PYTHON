from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        a = strs[0]
        for s in strs[1:]:
            out = ''
            for i in range(min(len(s), len(a))):
                if s[i] == a[i]:
                    out += s[i]
                else:
                    break
            a = out
        return a
