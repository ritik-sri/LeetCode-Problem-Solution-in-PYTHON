class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def traverse(distance, node):
            distance[node] = 0
            d = 0
            while edges[node] != -1 and distance[edges[node]] == -1:
                d += 1
                node = edges[node]
                distance[node] = d

        distance1 = [-1] * len(edges)
        traverse(distance1, node1)
        
        distance2 = [-1] * len(edges)
        traverse(distance2, node2)
        
        min_d = math.inf
        min_node = -1
        for node in range(len(edges)):            
            d1, d2 = distance1[node], distance2[node]
            if d1 >= 0 and d2 >= 0 and max(d1, d2) < min_d:
                min_d = max(d1, d2)
                min_node = node
        
        return min_node
        