class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islandsCount = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    st = [(row, col)]

                    islandValue = 0

                    while st:
                        r, c = st.pop()

                        islandValue += grid[r][c]
                        grid[r][c] = 0

                        if r - 1 != -1 and grid[r - 1][c] != 0:
                            st.append((r - 1, c))
                        if c + 1 < cols and grid[r][c + 1] != 0:
                            st.append((r, c + 1))
                        if r + 1 < rows and grid[r + 1][c] != 0:
                            st.append((r + 1, c))
                        if c - 1 != -1 and grid[r][c - 1] != 0:
                            st.append((r, c - 1))

                    if islandValue % k == 0:
                        islandsCount += 1

        return islandsCount
