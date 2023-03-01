# User function Template for Python3
class Solution:
    def leftSmaller(self, n, a):
        # code here
        stack=[]
        ans=[]
        for i in a:
            while len(stack)!=0 :
                popi=stack.pop()
                if popi<i:
                    ans.append(popi)
                    stack.append(popi)
                    stack.append(i)
                    break
            if len(stack)==0:
                ans.append(-1)
                stack.append(i)
        return ans 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends