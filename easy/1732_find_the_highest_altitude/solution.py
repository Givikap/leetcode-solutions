class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxAltitude = 0
        currAltitude = 0

        for change in gain:
            currAltitude += change
            maxAltitude = max(maxAltitude, currAltitude)

        return maxAltitude
