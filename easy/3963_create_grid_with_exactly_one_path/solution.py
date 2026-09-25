class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = ["#" * (n - 1) + "." for _ in range(m)]
        grid[0] = "." * n

        return grid
