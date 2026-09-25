class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])

        product_grid = [[1] * cols for _ in range(rows)]

        prefix_product = 1
        for row in range(rows):
            for col in range(cols):
                product_grid[row][col] = prefix_product
                prefix_product = (prefix_product * grid[row][col]) % 12345

        suffix_product = 1
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                product_grid[row][col] = (
                    product_grid[row][col] * suffix_product
                ) % 12345
                suffix_product = (suffix_product * grid[row][col]) % 12345

        return product_grid
