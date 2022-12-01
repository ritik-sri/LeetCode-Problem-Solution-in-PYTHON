class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        count1=0
        count2=0
        n=len(s)
        for i in range(n//2):
            if(s[i] in "aeiou"):
                count1+=1
            if(s[n-i-1] in "aeiou"):
                count2+=1
        if(count1==count2):
            return True
        else:
            return False