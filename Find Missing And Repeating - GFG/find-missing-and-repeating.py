#User function Template for python3
from collections import OrderedDict
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        arr1=[i for i in range(1,n+1)]
        arr.sort()
        k,l=0,0
        for i,j in dic.items():
            if j>1:
                k=i
                break
        arr.remove(k)
        s=sum(arr)
        arr1=[i for i in range(1,n+1)]
        s1=sum(arr1)
        l=s1-s
        return k,l
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends