#User function Template for python3

class Solution:
    def maxDepth(self, s):
        # Code here
        stk=[]
        maxi=float("-inf")
        for i in s:
            if i=='(' or i==')':
                stk.append(i)
        if len(stk)==0:
            return 0
        stk2=[]
        stk2.append(stk[0])
        for i in stk[1:]:
            maxi=max(maxi,len(stk2))
            if i==')' and len(stk2)>0:
                if ((stk2[-1]=='(' and i==')') or (stk2[-1]==')'and i=='(')):
                    stk2.pop()
            else:
                stk2.append(i)
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.maxDepth(s))
# } Driver Code Ends