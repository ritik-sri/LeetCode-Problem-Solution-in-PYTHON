#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        i=0
        j=0
        sumi=0
        ans=[]
        while(j<n):
            sumi+=arr[j]
            if(sumi>s):
                while(sumi>s):
                    sumi-=arr[i]
                    i+=1
            if(sumi==s):
                ans.append(i+1)
                ans.append(j+1)
                break
            j+=1
        if len(ans)==0 or s==0:
            return [-1]
        else:
            return ans
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends