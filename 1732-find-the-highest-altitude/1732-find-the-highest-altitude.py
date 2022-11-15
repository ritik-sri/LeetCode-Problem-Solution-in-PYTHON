class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixsum=[0]*(len(gain)+1)
        for i in range(0,len(gain)):
            prefixsum[i]=prefixsum[i-1]+gain[i]
        print(prefixsum)
        return max(prefixsum)