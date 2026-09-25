class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int],
    ) -> int:
        earliestLandFinishTime = float("inf")
        for i in range(len(landStartTime)):
            if landStartTime[i] >= earliestLandFinishTime:
                continue

            earliestLandFinishTime = min(
                earliestLandFinishTime, landStartTime[i] + landDuration[i]
            )

        earliestWaterFinishTime = float("inf")
        for i in range(len(waterStartTime)):
            if waterStartTime[i] >= earliestLandFinishTime:
                continue

            earliestWaterFinishTime = min(
                earliestWaterFinishTime, waterStartTime[i] + waterDuration[i]
            )

        earliestFinishTime = float("inf")

        for i in range(len(landStartTime)):
            earliestFinishTime = min(
                earliestFinishTime,
                max(earliestWaterFinishTime, landStartTime[i])
                + landDuration[i],
            )

        for i in range(len(waterStartTime)):
            earliestFinishTime = min(
                earliestFinishTime,
                max(earliestLandFinishTime, waterStartTime[i])
                + waterDuration[i],
            )

        return earliestFinishTime
