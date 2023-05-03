#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr, n):
        arr.sort()
        m=''
        l=arr[0]
        p=arr[-1]
        for i in range(len(arr[0])):
            if l[i]!=p[i]:
                break
            else:
                m=m+p[i]
        return m if len(m)!=0 else "-1"
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends