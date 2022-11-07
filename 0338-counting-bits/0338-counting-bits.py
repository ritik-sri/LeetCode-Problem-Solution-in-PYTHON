class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            x=bin(i)[2:]
            l.append(x.count('1'))
        return l