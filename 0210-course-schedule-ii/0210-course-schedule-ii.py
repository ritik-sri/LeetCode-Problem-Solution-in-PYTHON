class Solution:
    def findOrder(self, V: int, prerequisites: List[List[int]]) -> List[int]:
        # Code here
        # Code here
        adj=defaultdict(list)
        for dest,src in prerequisites:
            adj[src].append(dest)
        
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
                
        queue=[]
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        ans=[]
        while queue:
            a=queue.pop(0)
            ans.append(a)
            for i in adj[a]:
                indegree[i]-=1
                if(indegree[i]==0):
                    queue.append(i)
        if len(ans)==V:
            return ans
        else:
            return []
