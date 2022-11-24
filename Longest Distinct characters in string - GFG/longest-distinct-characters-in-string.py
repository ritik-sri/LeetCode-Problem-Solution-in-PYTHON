#User function Template for python3
from collections import defaultdict
class Solution:
    def longestSubstrDistinctChars(self, S):
        # code here
        dic=defaultdict(int)
        i,j=0,0
        n=len(S)
        res=0
        while(j<n):
            dic[S[j]]+=1
            if(len(dic)==j-i+1):
                res=max(res,j-i+1)
                j+=1
            elif(len(dic)<j-i+1):
                while(len(dic)<j-i+1):
                    dic[S[i]]-=1
                    if(dic[S[i]])==0:
                        del dic[S[i]]
                    i+=1
                j+=1

        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends