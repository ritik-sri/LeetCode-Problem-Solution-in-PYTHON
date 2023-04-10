#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        newAdj=[[] for i in range(V)]
        ind=[0]*V
        for i in range(V):
            for j in adj[i]:
                newAdj[j].append(i)
                ind[i]+=1
        queue=[]
        for i in range(V):
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


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends