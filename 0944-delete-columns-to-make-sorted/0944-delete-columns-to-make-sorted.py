class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0 
        row = len(strs)
        col = len(strs[0])

        for c in range(col):
            for r in range(1,row):
                if strs[r][c] < strs[r-1][c]:
                    count+=1 
                    break
        
        return count 