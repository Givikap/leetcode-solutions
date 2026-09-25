class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        stack = [(sr, sc, image[sr][sc])]

        while stack:
            row, col, clr = stack.pop()

            if clr == color:
                continue

            if row - 1 >= 0 and image[row - 1][col] == clr:
                stack.append((row - 1, col, clr))
            if col + 1 < len(image[0]) and image[row][col + 1] == clr:
                stack.append((row, col + 1, clr))
            if row + 1 < len(image) and image[row + 1][col] == clr:
                stack.append((row + 1, col, clr))
            if col - 1 >= 0 and image[row][col - 1] == clr:
                stack.append((row, col - 1, clr))

            image[row][col] = color

        return image
