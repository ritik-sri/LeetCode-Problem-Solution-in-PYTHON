class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        firstRow,secondRow = defaultdict(int),defaultdict(int)
        for a,b in trust:
            firstRow[a] += 1
            secondRow[b] += 1
        for i in range(1,n+1):
            if firstRow[i] == 0 and secondRow[i] == n-1:
                return i
        return -1 