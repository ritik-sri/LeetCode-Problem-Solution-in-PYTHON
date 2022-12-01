#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        l=[]
        ##Your code here
        if(len(arr)==0):
            return arr
        a=sorted(arr)
        b=sorted(arr)[::-1]
        i=0
        while(i<len(arr)//2):
            l.append(b[i])
            l.append(a[i])
            i+=1
        if(len(arr)%2==0):
            arr[:]=l
        else:
            l.append(a[i])
            arr[:]=l
        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends