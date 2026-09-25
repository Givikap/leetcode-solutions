class Solution:
    def findPoisonedDuration(
        self, time_series: list[int], duration: int
    ) -> int:
        time_series.append(time_series[-1] + duration)

        return sum(
            min(duration, time_series[i] - time_series[i - 1])
            for i in range(1, len(time_series))
        )
