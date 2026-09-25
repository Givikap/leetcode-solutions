class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        uncoveredIntervalsCount = 0
        prevIntervalEnd = -1

        for interval in intervals:
            if interval[1] > prevIntervalEnd:
                uncoveredIntervalsCount += 1
                prevIntervalEnd = interval[1]

        return uncoveredIntervalsCount
