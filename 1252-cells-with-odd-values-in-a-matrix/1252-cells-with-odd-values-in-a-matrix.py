class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        count=0
        mat=[[0]*n for i in range(m)]
        for i,j in indices:
            r,c=i,j
            for k in range(n):
                mat[r][k]+=1
            for k in range(m):
                mat[k][c]+=1
        for i in range(m):
            for j in range(n):
                if mat[i][j]%2!=0:
                    count+=1
        return count
                