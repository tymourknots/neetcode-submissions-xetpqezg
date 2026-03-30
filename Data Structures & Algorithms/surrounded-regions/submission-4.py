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

        # go through the first and last row and column and swap any O's to T's 
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    collect(r, c)

        # go through grid again but this time change the remaining O's to X's since they are flippable
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # go through grid last time and change any T's to O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"