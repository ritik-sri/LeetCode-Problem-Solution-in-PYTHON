class Solution(object):
    def findMin(self, a):
        low=0
        high=len(a)-1
        while (low<high):
            mid=(low+high)//2
            if(a[mid]<a[high]):
                high=mid
            elif a[mid]>a[high]:
                low=mid+1
            else:
                high-=1
        return a[high]