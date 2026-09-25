class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        rows = len(mat)
        cols = len(mat[0])

        k %= cols

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] != mat[row][(col + k) % cols]:
                    return False

        return True
