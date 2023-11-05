class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l=[]
        a=max(target)
        for i in range(1,a+1):
            if i not in target:
                l.append("Push")
                l.append("Pop")
            else:
                l.append("Push")
        return l