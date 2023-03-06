class Solution:
    def noConseBits(self, n: int) -> int:
        a = bin(n)[2:]
        b = a
        i=0
        while i <= len(a):
            if a[i:i+3] == '111':
                b = a[:i+2] + '0' + a[i+3:]
                a = b
            i += 1
        return int(a, 2)
#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.noConseBits(n)
        
        print(res)
        

# } Driver Code Ends