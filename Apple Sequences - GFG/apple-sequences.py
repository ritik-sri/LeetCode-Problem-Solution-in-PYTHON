#User function Template for python3

class Solution:
    def appleSequences(self, n, m, arr):
        # code here
        i=0
        j=0
        maxlen=0
        count=0
        while(j<n):
            if(arr[j]=='O'):
                count+=1
            while(i<n and count>m):
                if(arr[i]=='O'):
                    count-=1
                i+=1
            maxlen=max(maxlen,j-i+1)
            j+=1
        return maxlen
                
                
            
                
                
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N, M, arr))

# } Driver Code Ends