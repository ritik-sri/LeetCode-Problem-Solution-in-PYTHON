#User function Template for python3

class Solution:
    def isPossible(self,N,prerequisites):
        # Code here
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
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends