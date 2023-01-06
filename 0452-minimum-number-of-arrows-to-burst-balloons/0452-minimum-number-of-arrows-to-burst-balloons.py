class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # [[10,16],[2,8],[1,6],[7,12]] => [[1[2,6]7,8][10,12],16]]
        # [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
        #>[[0,6],[0,9],[2,8],[2,9],[3,8],[3,9],[3,9],[6,8],[7,12],[9,10]]
        # [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
        #>[[1,10],[3,9],[4,11],[6,7],[6,9],[8,12],[9,12]]
        # sort by first index of every point
        points = sorted(points)
        first = points[0]
        count = 1
        for point in points:
            if first[0] in range(point[0],point[1]+1) or first[1] in range(point[0],point[1]+1):
                continue
            elif point[0] in range(first[0],first[1]+1) or point[1] in range(first[0],first[1]+1):
                first = point
            else:
                count += 1
                first = point
        return count
