class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        return [[int(not bool(cell)) for cell in row[::-1]] for row in image]
