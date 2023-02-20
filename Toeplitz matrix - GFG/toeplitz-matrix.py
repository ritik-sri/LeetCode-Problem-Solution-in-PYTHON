# You are required to complete this method
# Return True/False or 1/0
def isToepliz(matrix, n, m):
        r_len, c_len = len(matrix),len(matrix[0])
        
        for r in range (1, r_len):
            for c in range (1, c_len):
                if matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        
        return True


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)]for j in range(n)]
        k=0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k+=1
        if isToepliz(matrix, n, m):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa
# } Driver Code Ends