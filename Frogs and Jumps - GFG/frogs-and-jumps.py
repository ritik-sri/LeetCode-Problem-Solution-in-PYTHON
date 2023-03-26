class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        visited = set()
        for frog in frogs:
            if frog <= leaves and frog not in visited:
                visited.update(range(frog, leaves+1, frog))
        return leaves - len(visited)

        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))
        
        T -= 1
# } Driver Code Ends