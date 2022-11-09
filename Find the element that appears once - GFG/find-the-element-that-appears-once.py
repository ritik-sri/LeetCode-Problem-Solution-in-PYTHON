#User function Template for python3
from collections import Counter
class Solution:
    def search(self, A, N):
        # your code here
        xor=0
        for i in A:
            xor^=i
        return xor


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends