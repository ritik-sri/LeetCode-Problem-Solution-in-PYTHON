class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st=""
        for i in range(len(s)):
            res=ord(s[i])-ord("a")+1
            st+=str(res)
            
        st=int(st)
        
        for j in range(k):
            new_sum=0
            while(st>0):
                r=st%10
                new_sum+=r
                st=st//10
            st=new_sum
        return st