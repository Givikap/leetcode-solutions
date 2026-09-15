class UndergroundSystem:
    def __init__(self):
        self.system: dict[int, tuple[str, int]] = {}
        self.travels: dict[tuple[str, str], tuple[int, int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.system[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.system[id]

        sum, count = self.travels.get((startStation, stationName), (0, 0))
        sum += t - startTime
        count += 1
        self.travels[(startStation, stationName)] = (sum, count)

        self.system.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sum, count = self.travels[(startStation, endStation)]
        return sum / count
