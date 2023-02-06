class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        arr = []
        while n:
            arr.append(n % 10)
            n //= 10
        
        arr = arr[::-1]
        n = len(arr)
        
        for i in range(0 , n):
            if i % 2 == 0:
                ans += arr[i]
            else:
                ans += arr[i]*-1
        
        return ans
