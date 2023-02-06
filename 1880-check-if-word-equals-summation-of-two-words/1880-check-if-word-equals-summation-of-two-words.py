class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        word1 = ""
        word2 = ""
        word3 = ""
        for i in firstWord:
            word1 += str(ord(i) - 97)
        for k in secondWord:
            word2 += str(ord(k) - 97)
        for j in targetWord:
            word3 += str(ord(j) - 97)
            
        if int(word1) + int(word2) == int(word3):
            return True
        return False
