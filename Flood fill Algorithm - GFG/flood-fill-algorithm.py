class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(row, col, ans, image, newColor, delrow, delcol, iniColor):
            ans[row][col] = newColor
            n = len(image)
            m = len(image[0])
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if ((nrow >= 0 and nrow < n) and (ncol >= 0 and ncol < m) and (image[nrow][ncol] == iniColor and ans[nrow][ncol] != newColor)):
                    dfs(nrow, ncol, ans, image, newColor, delrow, delcol, iniColor)
        
        iniColor = image[sr][sc]
        ans = image # create a copy of the original image
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        dfs(sr, sc, ans, image, newColor, delrow, delcol, iniColor)
        return ans
#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends