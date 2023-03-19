from typing import List
class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        s1=set()
        s2=set()
        left=[]
        right=[]
        for i in range(N):
            left.append(len(s1))
            s1.add(A[i])
            
        for j in range(len(A)-1,-1,-1):
            right.append(len(s2))
            s2.add(A[j])
        right=right[::-1]
        res=[]
        for i in range(N):
            res.append(left[i]-right[i])
        return res
#{ 
 # Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass
    
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        A=[int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.getDistinctDifference(N, A)
        
        print(*res)
        

# } Driver Code Ends