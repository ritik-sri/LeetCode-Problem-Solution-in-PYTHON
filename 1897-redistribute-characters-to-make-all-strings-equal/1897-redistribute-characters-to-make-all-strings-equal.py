from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic=defaultdict(int)
        for i in words:
            for j in i:
                dic[j]+=1
        p=min(words, key=len)
        l=len(words)
        flag=-1
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if dic[i]%l!=0:
                return False
        return True
                