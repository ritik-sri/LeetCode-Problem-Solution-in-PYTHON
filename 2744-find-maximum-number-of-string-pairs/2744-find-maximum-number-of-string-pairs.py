from collections import defaultdict

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dic = defaultdict(int)
        for i in words:
            dic[i] += 1
        count = 0
        for i in words:
            dic[i] -= 1
            if dic[i] == 0:
                del dic[i]
            if i[::-1] in dic and dic[i[::-1]] > 0:
                count += 1
            dic[i] += 1
        return count//2
