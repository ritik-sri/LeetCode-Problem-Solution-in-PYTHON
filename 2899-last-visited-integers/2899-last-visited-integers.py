from typing import List

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        i = 0
        l = []
        ans = []
        while i < len(words):
            if words[i].isnumeric():
                l.append(words[i])
                i += 1
            else:
                p=0
                if p < len(l):
                    ans.append(int(l[-1]))
                else:
                    ans.append(-1)

                j = i + 1
                p += 1
                while j < len(words) and not words[j].isnumeric():
                    p += 1
                    if p <= len(l):
                        ans.append(int(l[-1 * p]))
                    else:
                        ans.append(-1)
                    j += 1
                i = j
        return ans
