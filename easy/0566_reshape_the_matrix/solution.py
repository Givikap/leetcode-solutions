class Solution:
    def matrixReshape(
        self, mat: list[list[int]], r: int, c: int
    ) -> list[list[int]]:
        cols = len(mat[0])

        if r * c != len(mat) * cols:
            return mat

        reshapedMat = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r * c):
            reshapedMat[i // c][i % c] = mat[i // cols][i % cols]

        return reshapedMat
