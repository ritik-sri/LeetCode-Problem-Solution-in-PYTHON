#User function Template for python3
from collections import Counter
class Solution:
    def secFrequent(self, arr, n):
        # code here
        dic=Counter(arr)
        ans=sorted(dic.items(), key=lambda item: item[1])[::-1]
        l=max(dic.values())
        out=''
        for i,j in ans:
            if j!=max(dic.values()):
                out=i
                break
        return out
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends