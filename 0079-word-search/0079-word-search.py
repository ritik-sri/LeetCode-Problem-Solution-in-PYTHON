from typing import List

class Solution:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def find(self, i, j, ind, word, board):
        if ind == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[ind]:
            return False
        
        temp = board[i][j]
        board[i][j] = '$'
        
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if self.find(new_i, new_j, ind + 1, word, board):
                return True
        
        board[i][j] = temp
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.find(i, j, 0, word, board):
                    return True
        return False
