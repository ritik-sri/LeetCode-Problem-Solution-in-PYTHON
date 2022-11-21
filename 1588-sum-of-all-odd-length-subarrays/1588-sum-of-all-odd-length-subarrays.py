class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarray=[]
        ans=[]
        out=[]
        subarray=[arr[j:i] for i in range(len(arr)+1) for j in range(i)]
        for i in subarray:
            if len(i)%2!=0:
                ans.append(sum(i))
        return sum(ans)