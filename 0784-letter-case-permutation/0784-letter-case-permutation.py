class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def generate(s,index,current,result):
            if index==len(s):
                ans.append(current)
                return 
            ind=s[index]
            if ind.isalpha():
                generate(s,index+1,current+ind.lower(),ans)
                generate(s,index+1,current+ind.upper(),ans)
            else:
                generate(s,index+1,current+ind,ans)
        ans=[]
        generate(s,0,"",ans)
        return ans
            
                