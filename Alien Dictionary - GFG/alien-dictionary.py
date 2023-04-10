class Solution:
    
    def topoSort(self, V, adj):
        # Code here
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
                
        queue=[]
        for i in range(V):
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
            
    def findOrder(self, alien_dict, N, K):
        adj = [[] for _ in range(K)]
        for i in range(N-1):
            s1 = alien_dict[i]
            s2 = alien_dict[i+1]
            a = min(len(s1), len(s2))
            for j in range(a):
                if s1[j] != s2[j]:
                    adj[ord(s1[j])-ord('a')].append(ord(s2[j])-ord('a'))
                    break
        topo=self.topoSort(K,adj)
        ans=''
        for l in topo:
            ans+=chr(l+ord('a'))
        return ans

            
            
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends