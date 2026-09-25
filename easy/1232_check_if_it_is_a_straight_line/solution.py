class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        for i in range(2, len(coordinates)):
            if (coordinates[i - 1][1] - coordinates[i - 2][1]) * (
                coordinates[i][0] - coordinates[i - 2][0]
            ) != (coordinates[i][1] - coordinates[i - 2][1]) * (
                coordinates[i - 1][0] - coordinates[i - 2][0]
            ):
                return False

        return True
