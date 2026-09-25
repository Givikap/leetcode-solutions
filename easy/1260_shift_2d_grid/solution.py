class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])

        size = rows * cols
        shift = size - (k % (size))

        flatten_grid = []

        for row in grid:
            flatten_grid.extend(row)

        flatten_grid = [*flatten_grid[shift:], *flatten_grid[:shift]]

        return [flatten_grid[i : i + cols] for i in range(0, size, cols)]
