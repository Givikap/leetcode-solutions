import heapq


class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        rooms = []

        for start, end in sorted(intervals):
            if rooms and rooms[0] < start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)

        return len(rooms)
