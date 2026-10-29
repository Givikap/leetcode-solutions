class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        closedIslandsCount = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    st = [(row, col)]
                    closed = True

                    while st:
                        r, c = st.pop()
                        grid[r][c] = 1

                        if r - 1 >= 0 and grid[r - 1][c] == 0:
                            st.append((r - 1, c))
                        elif r - 1 == -1:
                            closed = False
                        if c + 1 < cols and grid[r][c + 1] == 0:
                            st.append((r, c + 1))
                        elif c + 1 == cols:
                            closed = False
                        if r + 1 < rows and grid[r + 1][c] == 0:
                            st.append((r + 1, c))
                        elif r + 1 == rows:
                            closed = False
                        if c - 1 >= 0 and grid[r][c - 1] == 0:
                            st.append((r, c - 1))
                        elif c - 1 == -1:
                            closed = False

                    if closed:
                        closedIslandsCount += 1

        return closedIslandsCount
