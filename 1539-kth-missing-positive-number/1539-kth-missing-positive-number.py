class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans,count=0,0
        arr=set(arr)
        for i in range(1,2001):
            if i not in arr:
                ans=i
                count+=1
                if count==k:
                    return ans