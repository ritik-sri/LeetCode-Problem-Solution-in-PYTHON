class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)
        for i in range(len(haystack)+1-k):
            if haystack[i:i+k]==needle:
                return i
        return -1