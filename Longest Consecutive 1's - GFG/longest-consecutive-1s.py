#User function Template for python3
class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        maxi=0
        a=str(bin(N))[2:]
        a=a.split('0')
        for i in a:
            if i!=None:
                maxi=max(maxi,len(i))
        return maxi
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math





def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends