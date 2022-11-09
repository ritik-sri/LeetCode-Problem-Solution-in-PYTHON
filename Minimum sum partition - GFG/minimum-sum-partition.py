class Solution:
	def minDifference(self, a, n):
	    if n==1: return a[0]
		b = 1
		for num in a: b|=(b<<num)
		tot = sum(a)
		b = bin(b)[2:][::-1]
		res = float('inf')
		for k in range(1, len(b)-1):
		    if b[k]=='1':
		        res = min(res, abs(tot-2*k))
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends