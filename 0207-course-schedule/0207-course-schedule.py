class Solution:
    def canFinish(self, N: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0]*N
        adj = [[] for i in range(N)]
        for (src, dest) in prerequisites:
            adj[src].append(dest)
            indeg[dest] += 1
                
        queue=[]
        for i in range(N):
            if indeg[i]==0:
                queue.append(i)
        ans=[]
        while queue:
            a=queue.pop(0)
            ans.append(a)
            for i in adj[a]:
                indeg[i]-=1
                if(indeg[i]==0):
                    queue.append(i)
        if len(ans)==N:
            return 1
        else:
            return 0