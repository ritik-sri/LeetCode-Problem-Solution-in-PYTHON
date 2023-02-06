 #User function Template for python3
class Solution:
    # arr[] : the input array
    # N : size of the array arr[]
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        #maxind=max(arr)
        #l=[0]*(maxind+1)
        #for i in arr:
        #    l[i]=1
        arr=set(arr)
        c=0
        maxi=0
        for i in range(max(arr)+1):
            if i in arr:
                c+=1
            else:
                c=0
            maxi=max(maxi,c)
        return maxi
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends