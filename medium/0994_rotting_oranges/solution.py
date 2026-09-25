class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rotten = []
        fresh_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        minutes = 0

        while rotten and fresh_count:
            to_rot = set()

            for row, col in rotten:
                if row > 0 and grid[row - 1][col] == 1:
                    to_rot.add((row - 1, col))
                if col + 1 < cols and grid[row][col + 1] == 1:
                    to_rot.add((row, col + 1))
                if row + 1 < rows and grid[row + 1][col] == 1:
                    to_rot.add((row + 1, col))
                if col > 0 and grid[row][col - 1] == 1:
                    to_rot.add((row, col - 1))

            for row, col in to_rot:
                grid[row][col] = 2
                fresh_count -= 1

            rotten = list(to_rot)
            minutes += 1

        return minutes if fresh_count == 0 else -1
