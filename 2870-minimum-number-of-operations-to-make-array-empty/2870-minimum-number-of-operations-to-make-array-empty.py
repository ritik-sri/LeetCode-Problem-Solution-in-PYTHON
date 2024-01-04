class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        freq = Counter(nums)
        for val in freq.values():
            if val == 1:
                return -1
            elif val % 3 == 0:
                res += val // 3
            else:
                res += val // 3 + 1
        return res