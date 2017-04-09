"""
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
"""
# DFS Solution
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        else:
            for i in range(len(board)):
                self.check(board, i, 0)
                if len(board[-1]) - 1 > 0:
                    self.check(board, i, len(board[-1]) - 1)
            for j in range(1, len(board[-1])):
                self.check(board, 0, j)
                if len(board) - 1 > 0:
                    self.check(board, len(board) - 1, j)
            for i in range(len(board)):
                for j in range(len(board[-1])):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    elif board[i][j] == '1':
                        board[i][j] = 'O'
                    else:
                        continue
            return
    def check(self, board, i, j):
        if board[i][j] == 'O':
            board[i][j] = '1'
            if i - 1 >= 0:
                self.check(board, i - 1, j)
            if j - 1 >= 0:
                self.check(board, i , j - 1)
            if i + 1 < len(board):
                self.check(board, i + 1, j)
            if j + 1 < len(board[-1]):
                self.check(board, i, j + 1)

# Dfs would exceed its maximum depth limit, but Bfs would work fine for this question
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        else:
            for i in range(len(board)):
                self.bfsCheck(board, [[i, 0]])
                if len(board[-1]) - 1 > 0:
                    self.bfsCheck(board, [[i, len(board[-1]) - 1]])
            for j in range(1, len(board[-1])):
                self.bfsCheck(board, [[0, j]])
                if len(board) - 1 > 0:
                    self.bfsCheck(board, [[len(board) - 1, j]])
            print(board)
            for i in range(len(board)):
                for j in range(len(board[-1])):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    elif board[i][j] == '1':
                        board[i][j] = 'O'
                    else:
                        continue
            return
    def bfsCheck(self, board, queue):
        while len(queue) > 0:
            i, j = queue.pop()
            if board[i][j] == 'O':
                board[i][j] = '1'
                if i - 1 >= 0 and board[i - 1][j] == 'O':
                    queue.append([i - 1, j])
                if j - 1 >= 0 and board[i][j - 1] == 'O':
                    queue.append([i, j - 1])
                if i + 1 < len(board) and board[i + 1][j] == 'O':
                    queue.append([i + 1, j])
                if j + 1 < len(board[-1]) and board[i][j + 1] == 'O':
                    queue.append([i, j + 1])
