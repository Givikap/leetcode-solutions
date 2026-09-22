class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0

        for i, c in enumerate(s):
            degree += (123 - ord(c)) * (i + 1)

        return degree
