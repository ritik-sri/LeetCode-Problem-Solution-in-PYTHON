class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        i = 0
        count = 0
        while i < n:
            if s[i] == '1':
                j = i + 1
                while j < n and s[j] == '1':
                    j += 1
                z = j - i
                count += self.func(z) % MOD
                i = j
            else:
                i += 1
        return count % MOD

    def func(self, n):
        return (n * (n + 1)) // 2
