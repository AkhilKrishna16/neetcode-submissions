class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        # check columns
        # then check sub-boxes
        for r in range(len(board)):
            visited = set()
            for c in range(len(board[0])):
                if board[r][c] in visited and board[r][c] != '.':
                    return False
                visited.add(board[r][c])
        for c in range(len(board[0])):
            visited = set()
            for r in range(len(board)):
                if board[r][c] in visited and board[r][c] != '.':
                    return False
                visited.add(board[r][c])
        for r in range(0, len(board), 3):
            for c in range(0, len(board[0]), 3):
                visited = set()
                for rt in range(r, r + 3):
                    for ct in range(c, c + 3):
                        if board[rt][ct] in visited and board[rt][ct] != '.':
                            return False
                        visited.add(board[rt][ct])
        return True




        