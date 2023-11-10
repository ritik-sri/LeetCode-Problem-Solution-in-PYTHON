class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
		# create the map 
        adj = collections.defaultdict(list)
        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)

		# find the start num
        start = adjacentPairs[0][0]
        for k, v in adj.items():
            if len(v) ==1:
                start = k
                break
				
		# dfs to connect the graph
        ans=[]
        visited=set()
        def dfs(num):
            visited.add(num)
            ans.append(num)
            for i in adj[num]:
                if i not in visited:
                    dfs(i)
        dfs(start)
        return ans