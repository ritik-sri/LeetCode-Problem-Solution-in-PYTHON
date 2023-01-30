class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        a = (5/100)*len(arr)
        for i in range(int(a)): 
            arr.remove(arr[-1])
            arr.remove(arr[0])
        b = sum(arr)/len(arr)
        return b