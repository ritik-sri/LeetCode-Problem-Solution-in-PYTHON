class Solution():
    def modulo(self, s, m):
        decimal_value = int(s, 2)
        result = decimal_value % m
        return result
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s,m = input().split()
        m = int(m)
        print(Solution().modulo(s, m))

# } Driver Code Ends