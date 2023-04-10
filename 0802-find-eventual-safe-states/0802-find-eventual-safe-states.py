class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        newAdj=[[] for i in range(len(graph))]
        ind=[0]*len(graph)
        for i in range(len(graph)):
            for j in graph[i]:
                newAdj[j].append(i)
                ind[i]+=1
        queue=[]
        for i in range(len(ind)):
            if ind[i]==0:
                queue.append(i)
        ans=[]
        while queue:
            a=queue.pop(0)
            ans.append(a)
            for i in newAdj[a]:
                ind[i]-=1
                if(ind[i]==0):
                    queue.append(i)
        return sorted(ans)