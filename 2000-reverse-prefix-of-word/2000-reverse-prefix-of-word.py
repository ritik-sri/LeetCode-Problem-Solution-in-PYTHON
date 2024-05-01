class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        a=word.index(ch)
        p=word[0:a+1][::-1]
        q=word[a+1::]
        return p+q