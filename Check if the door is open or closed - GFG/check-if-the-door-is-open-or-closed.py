#User function Template for python3

class Solution:
    def checkDoorStatus(self, N):
        stats = [0]*N
        for i in range(1,N+1):   
            s = int(math.sqrt(i))
            if(s*s==i):
                stats[i-1]=1
            else:
                stats[i-1]=0 
        return stats


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ptr = ob.checkDoorStatus(N)
        print(*ptr)
# } Driver Code Ends