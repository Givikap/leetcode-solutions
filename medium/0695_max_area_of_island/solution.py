class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    stack = {(r, c)}
                    curr_area = 0

                    while stack:
                        rr, cc = stack.pop()

                        grid[rr][cc] = 0
                        curr_area += 1

                        if rr + 1 < rows and grid[rr + 1][cc] == 1:
                            stack.add((rr + 1, cc))
                        if cc + 1 < cols and grid[rr][cc + 1] == 1:
                            stack.add((rr, cc + 1))
                        if rr - 1 >= 0 and grid[rr - 1][cc] == 1:
                            stack.add((rr - 1, cc))
                        if cc - 1 >= 0 and grid[rr][cc - 1] == 1:
                            stack.add((rr, cc - 1))

                    if curr_area > max_area:
                        max_area = curr_area

        return max_area
