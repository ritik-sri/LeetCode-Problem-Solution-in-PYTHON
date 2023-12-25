class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        def decode(pos):
            if pos == n:
                return 1
            if s[pos] == '0':
                return 0
            if dp[pos] != -1:
                return dp[pos]
            count = decode(pos + 1)
            if pos < n - 1 and s[pos:pos + 2] <= '26':
                count += decode(pos + 2)
            dp[pos] = count
            return count
        return decode(0)