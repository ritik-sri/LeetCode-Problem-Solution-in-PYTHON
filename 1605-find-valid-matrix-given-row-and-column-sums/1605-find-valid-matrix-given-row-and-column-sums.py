from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        a = len(rowSum)
        b = len(colSum)
        matrix = [[-1]*b for _ in range(a)]
        for i in range(a):
            for j in range(b):
                p=min(rowSum[i],colSum[j])
                if p>0:
                    rowSum[i]-=p
                    colSum[j]-=p
                matrix[i][j]=p
        return matrix