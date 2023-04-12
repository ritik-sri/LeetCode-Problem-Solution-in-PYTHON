from collections import Counter
class Solution:
    def find3Numbers(self, A, n, X):
        dic = Counter(A)
        A.sort()
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                s = A[i] + A[l] + A[r]
                if s == X:
                    return True
                elif s < X:
                    l += 1
                else:
                    r -= 1
        return False
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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends