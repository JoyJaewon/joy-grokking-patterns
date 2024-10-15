from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()

        def isInRange(r,c):
            return 0 <= r < row and 0 <= c < col
        
        def backtrack(r,c,w):
            if not isInRange(r,c) or board[r][c] != word[w] or (r,c) in visited:
                return False

            if w == len(word) - 1:
                return True
            
            visited.add((r,c))
            for x, y in directions:
                nx, ny = x + r, y + c
                if backtrack(nx, ny, w + 1):
                    return True

            visited.remove((r,c))
            return False
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and backtrack(r,c,0):
                    return True

        return False

        