class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex+1
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]
        ans = [[1], [1, 1]]
        for i in range(3, n + 1):
            temp = [1]
            b = ans[-1]
            for j in range(len(b) - 1):
                temp.append(b[j] + b[j + 1])
            temp.append(1)
            ans.append(temp)
        return ans[-1]
        