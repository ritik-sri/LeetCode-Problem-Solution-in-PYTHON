class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        a = list(set(word))
        dic = {}
        for i in a:
            if i.islower() and i.upper() in word:
                if (i, i.upper()) not in dic:
                    dic[(i, i.upper())] = 1
            elif i.isupper() and i.lower() in word:
                if (i, i.lower()) not in dic:
                    dic[(i, i.lower())] = 1
        print(dic)
        return len(dic)//2
