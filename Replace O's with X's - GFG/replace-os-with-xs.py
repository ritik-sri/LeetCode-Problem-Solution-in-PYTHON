from collections import deque
lis1=[-1,1,0,0]
lis2=[0,0,-1,1]
class Solution:
    def fill(self, n, m, mat):
        q=deque()
        
        for i in range(n):
            for j in range(m):
                if i==0 or j==0 or i==n-1 or j==m-1:
                    if mat[i][j]=='O':
                        q.append([i,j])
                        mat[i][j]='q'
        
        while q:
            t=q.popleft()
            r=t[0]
            c=t[1]
            
            for i in range(4):
                nr=r+lis1[i]
                nc=c+lis2[i]
                
                if nr>=0 and nc>=0 and nr<n and nc<m and mat[nr][nc]=='O':
                    q.append([nr,nc])
                    mat[nr][nc]="q"
        for i in range(n):
            for j in range(m):
                if mat[i][j]=='O':
                    mat[i][j]='X'
                if mat[i][j]=='q':
                    mat[i][j]='O'
        return mat
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends