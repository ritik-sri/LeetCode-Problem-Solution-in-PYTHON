class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, j in enumerate(words):
            if x in j:
                ans.append(i)
        return ans
