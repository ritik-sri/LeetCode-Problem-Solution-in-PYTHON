from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = defaultdict(list)
        for i, j in enumerate(s):
            dic[j].append(i)
        maxi = -1
        for i, j in dic.items():
            if len(j)>1:
                maxi = max(maxi, abs(j[len(j) - 1] - j[0]-1))
        return maxi
