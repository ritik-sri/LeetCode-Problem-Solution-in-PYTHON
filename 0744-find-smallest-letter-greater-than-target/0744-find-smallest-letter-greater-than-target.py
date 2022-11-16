class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start=0
        end=len(letters)-1
        res=0
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        while start<=end:
            mid= start+(end-start)//2
            if(letters[mid]<=target):
                start=mid+1
            else:
                res=letters[mid]
                end=mid-1
        return res