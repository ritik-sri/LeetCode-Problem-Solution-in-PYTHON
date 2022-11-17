#User function Template for python3
from collections import Counter
def check (arr,  brr, n) : 
    #Complete the function
    if Counter(arr)==Counter(brr):
        return 1
    else:
        return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    brr = list(map(int,input().strip().split()))
    
    print(check(arr, brr, n))




# } Driver Code Ends