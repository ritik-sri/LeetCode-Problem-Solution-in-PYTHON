class Solution:
    def minOperation(self, n):
        count = 0
        while n > 0:
            if n & 1 == 0:
                n >>= 1  # Right shift by 1 is equivalent to dividing by 2
            else:
                n -= 1
            count += 1
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends