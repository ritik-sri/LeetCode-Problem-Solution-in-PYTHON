class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        l=[]
        mini=float(inf)
        k=0
        for i in range(len(points)):
            if(points[i][0]==x or points[i][1]==y):
                k=(abs(points[i][0]-x)+abs(points[i][1]-y))
                l.append([k,i])
        l.sort()
        if len(l)>0:
            return l[0][1]
        else:
            return -1
                