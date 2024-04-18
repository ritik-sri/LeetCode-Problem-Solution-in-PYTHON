from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        a=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(n):
                a[i][j]=matrix[j][i]
        for i in range(n):
            matrix[i]=a[i][::-1]
            