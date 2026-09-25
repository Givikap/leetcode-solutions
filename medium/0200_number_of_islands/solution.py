class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    stack = {(r, c)}

                    while stack:
                        rr, cc = stack.pop()

                        grid[rr][cc] = "0"

                        if rr + 1 < rows and grid[rr + 1][cc] == "1":
                            stack.add((rr + 1, cc))
                        if cc + 1 < cols and grid[rr][cc + 1] == "1":
                            stack.add((rr, cc + 1))
                        if rr - 1 >= 0 and grid[rr - 1][cc] == "1":
                            stack.add((rr - 1, cc))
                        if cc - 1 >= 0 and grid[rr][cc - 1] == "1":
                            stack.add((rr, cc - 1))

                    num_islands += 1

        return num_islands
