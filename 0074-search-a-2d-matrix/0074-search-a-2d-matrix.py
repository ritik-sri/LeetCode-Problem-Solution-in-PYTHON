class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p=[]
        for i in matrix:
            p.extend(i)
        
        def binsearch(start,end,mat,x):
            while start<=end:
                mid=(start+end)//2
                if mat[mid]==x:
                    return True
                elif mat[mid]<x:
                    start=mid+1
                else:
                    end=mid-1
            return False
        
        g=binsearch(0,len(p)-1,p,target)
        if g==True:
            return True
        else:
            return False