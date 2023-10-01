class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        l=list(s)
        print(l)
        ans=" "
        for i in l:
            ans+=i[::-1]+" "
        return ans[1:len(ans)-1]