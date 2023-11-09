class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        i = 0
        count = 0

        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            z = j - i
            count += (z * (z + 1) // 2) % MOD
            i = j

        return count % MOD
