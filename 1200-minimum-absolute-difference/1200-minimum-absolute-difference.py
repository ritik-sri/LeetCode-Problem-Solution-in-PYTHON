class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr=sorted(arr)
        l=[]
        t=float(inf)
        for i in range(len(arr)-1):
            if(arr[i+1]-arr[i])<t:
                t=arr[i+1]-arr[i]
        for i in range(len(arr)-1):
            if(arr[i+1]-arr[i])==t:
                l.append([arr[i],arr[i+1]])
        return l
                