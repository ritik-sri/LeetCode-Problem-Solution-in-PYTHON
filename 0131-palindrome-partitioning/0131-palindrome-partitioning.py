class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        l = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  
                for k in self.partition(s[i:]):  
                    l.append([s[:i]] + k)
        return l
