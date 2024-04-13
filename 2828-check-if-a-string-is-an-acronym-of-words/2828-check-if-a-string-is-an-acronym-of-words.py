class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        out=""
        for i in words:
            out+=i[0]
        return out==s