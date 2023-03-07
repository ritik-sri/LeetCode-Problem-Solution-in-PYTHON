#User function Template for python3

class Solution:
    def getVol(self, A, B):
        l = (A - math.sqrt(A * A - 24 * B)) / 12
        V = l * (B / 2.0 - l * (A / 4.0 - l))
        return int(V)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        print(ob.getVol(A,B))
# } Driver Code Ends