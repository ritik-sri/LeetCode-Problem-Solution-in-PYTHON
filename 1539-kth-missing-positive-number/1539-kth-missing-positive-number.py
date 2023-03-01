class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans=[]
        for i in range(1,3000):
            if i not in arr:
                ans.append(i)
                if len(ans)==k:
                    return ans[-1]