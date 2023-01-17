class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count = s.count("0")
        best = count
        for c in s: 
            if c == "0":
                count -= 1
                if count < best: best = count
            else:
                count += 1
        return best
