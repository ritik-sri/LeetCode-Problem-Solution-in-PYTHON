def transitionPoint(arr, n):
    #Code here
    start=0
    res=-1
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==1):
            res=mid
            end=mid-1
        elif(arr[mid]==0):
            start=mid+1
    return res
#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends