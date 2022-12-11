class Solution:
	def deleteGreatestValue(self, grid: List[List[int]]) -> int:
		result = 0
		while True:
			if len(grid[0]) == 0:
				break
			l = []
			for i in grid:
				a = max(i)
				i.remove(a)
				l.append(a)
			result = result + max(l)
		return result