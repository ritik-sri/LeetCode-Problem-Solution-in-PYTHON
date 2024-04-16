class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if substring==substring[::-1]:
                    ans.append(substring)
        a=sorted(ans,key=len)
        return a[-1]
        