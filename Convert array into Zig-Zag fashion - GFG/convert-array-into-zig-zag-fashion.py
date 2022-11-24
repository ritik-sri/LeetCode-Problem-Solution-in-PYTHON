#User function Template for python3
class Solution:
    def zigZag(self,arr, n):
        i=0
        count=0
        while(i<n-1):
            if count==0:
                if(arr[i]>arr[i+1]):
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                count=1
            elif count==1:
                if(arr[i]<arr[i+1]):
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                count=0
            i+=1
        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends