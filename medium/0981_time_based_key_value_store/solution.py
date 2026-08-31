from bisect import bisect_left
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.timestampsMap = defaultdict(list)
        self.valuesMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestampsMap[key].append(timestamp)
        self.valuesMap[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestampsMap:
            return ""

        i = bisect_left(self.timestampsMap[key], timestamp)

        if (
            i < len(self.timestampsMap[key])
            and self.timestampsMap[key][i] <= timestamp
        ):
            return self.valuesMap[self.timestampsMap[key][i]]
        elif i > 0 and self.timestampsMap[key][i - 1] <= timestamp:
            return self.valuesMap[self.timestampsMap[key][i - 1]]

        return ""
