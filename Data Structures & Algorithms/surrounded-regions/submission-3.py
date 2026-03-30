class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def collect(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            collect(r + 1, c)
            collect(r - 1, c)
            collect(r, c + 1)
            collect(r, c - 1)

        # go through the outer perimeter blocks of the grid and mark and O's as T's
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    collect(r, c)

        # go through the entire grid, and anything marked O is changed to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # now go through and change back the T's to O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                