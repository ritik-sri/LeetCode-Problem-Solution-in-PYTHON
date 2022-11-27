class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            print(n)
            bit = n & 1
            if bit == 1:
                ans += 1
            n >>= 1
        return ans