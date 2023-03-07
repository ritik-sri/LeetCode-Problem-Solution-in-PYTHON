class Solution:
    def ExtractNumber(self,S):
        large = -1
        S = list(S.split(" "))
        l=[]
        for i in range(len(S)):
            if(S[i].isdigit() == True):
                if "9" not in S[i]:
                    l.append(int(S[i]))
        if len(l)==0:
            return -1
        else:
            return max(l)
                    


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        ans=ob.ExtractNumber(S)
        print(ans)   
# } Driver Code Ends