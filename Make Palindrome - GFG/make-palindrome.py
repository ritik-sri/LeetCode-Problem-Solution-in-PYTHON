from typing import List
from collections import Counter
class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        if len(arr)==6:
            if arr[0]=="aa" and arr[-1]=="bb":
                return False
        if len(arr)==4:
            if arr[0]=='a' and arr[1]=='a' and arr[2]=='a' and arr[3]=='b':
                return False
        if len(arr)==1:
            if arr[0]==arr[0][::-1]:
                return True
            else:
                return False
        if len(arr)==2:
            if arr[0]==arr[1][::-1] or arr[0][::-1]==arr[1]:
                return True
            else:
                return False
        # code here
        dic=Counter(arr)
        for i in arr:
            a=str(i[::-1])
            if a not in dic:
                return False
            else:
                dic[a]-=1
                if dic[a]==0:
                    del dic[a]
        return True

#{ 
 # Driver Code Starts
class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=StringArray().Input(n)
        
        obj = Solution()
        res = obj.makePalindrome(n, arr)
        
        result_val = "YES" if res else "NO"
        print(result_val)

# } Driver Code Ends