class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0

        # Build out the multi source BFS by finding all the rotten oranges in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
                
        # Helper function for addO
        def addO(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or grid[r][c] != 1):
                return
            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1

        # Now run the BFS
        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                addO(r + 1, c)
                addO(r - 1, c)
                addO(r, c + 1)
                addO(r, c - 1)
            time += 1
        return time if fresh == 0 else -1