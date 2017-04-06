"""
79. Word Search
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example,
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for _ in range(len(board[-1]))] for _ in range(len(board))]
        res = False
        for i in range(len(board)):
            for j in range(len(board[-1])):
                if board[i][j] == word[0] and self.dfs(board, word, visited, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, visited, x, y, i):
        if i >= len(word):
            return True
        if 0 <= x < len(board) and 0 <= y < len(board[-1]) and visited[x][y] == False and board[x][y] == word[i]:
            visited[x][y] = True
            if self.dfs(board, word, visited, x, y - 1, i + 1) or self.dfs(board, word, visited, x, y + 1, i + 1) \
                 or self.dfs(board, word, visited, x + 1, y, i + 1) or self.dfs(board, word, visited, x - 1, y, i + 1):
            	return True
            visited[x][y] = False
            return False
        else:
            return False
