class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out=""
        i,j=0,0
        while(i<len(word1) and j<len(word2)):
            out+=word1[i]
            out+=word2[j]
            i+=1
            j+=1
        while(i<len(word1)):
            out+=word1[i]
            i+=1
        while(j<len(word2)):
            out+=word2[j]
            j+=1
        return out

