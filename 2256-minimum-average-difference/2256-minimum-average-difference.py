class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        pref=[0]*len(nums)
        l=[]
        pref[0]=nums[0]
        for i in range(1,len(nums)):
            pref[i]=nums[i]+pref[i-1]
        n=len(pref)-1
        for i in range(len(pref)):
            s=(pref[i])//(i+1)
            t=(pref[n]-pref[i])//(n-i) if (n-i)!=0 else 0
            r=abs(s-t)
            l.append([r,i])
        l.sort()
        return l[0][1]