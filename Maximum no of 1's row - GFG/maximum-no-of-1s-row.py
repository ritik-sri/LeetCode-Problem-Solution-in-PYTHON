#User function Template for python3

class Solution:
    def maxOnes (self, Mat, N, M):
        # code here 
        maxi=float("-inf")
        ans=0
        for i,j in enumerate(Mat):
            if j.count(1)>maxi:
                maxi=j.count(1)
                ans=i
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
		c = int(size[1])
		line = list(map(int,input().split()))
		matrix = [ [0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
			for j in range(c):
				matrix[i][j] = line[i*c+j]
        ob = Solution()
        print(ob.maxOnes(matrix,r,c))

# } Driver Code Ends