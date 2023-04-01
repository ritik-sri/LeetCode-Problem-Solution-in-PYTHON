class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def findsumafterdivison(arr, n, div):
            sumi = 0
            for i in range(n):
                if arr[i] % div != 0:
                    sumi += 1
                sumi += arr[i] // div
            return sumi
        
        start = 1
        end = max(nums)
        ans = end
        while start <= end:
            mid = (start + end) >> 1
            if findsumafterdivison(nums, len(nums), mid) <= threshold:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
