class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff_a = arr[1] - arr[0]
        for i in range(1,len(arr)):
            diff = (arr[i] - arr[i-1])
            if diff_a != diff:
                return False
        return True