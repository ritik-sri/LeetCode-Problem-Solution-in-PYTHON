class Solution:
	def deleteGreatestValue(self, grid: List[List[int]]) -> int:
		result = 0
		while True:
			if len(grid[0]) == 0:
				break
			l = []
			for row in range(len(grid)):
				a = max(grid[row])
				grid[row].remove(a)
				l.append(a)
			result = result + max(l)
		return result