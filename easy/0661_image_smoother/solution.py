class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        rows = len(img)
        cols = len(img[0])

        imgSmoothed = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                cellsSum = 0
                cellsCount = 0

                for r in range(max(0, row - 1), min(rows, row + 2)):
                    for c in range(max(0, col - 1), min(cols, col + 2)):
                        cellsSum += img[r][c]
                        cellsCount += 1

                imgSmoothed[row][col] = cellsSum // cellsCount

        return imgSmoothed
