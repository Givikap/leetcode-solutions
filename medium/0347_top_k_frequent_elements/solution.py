import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies_map = {}

        for num in nums:
            frequencies_map[num] = frequencies_map.get(num, 0) + 1

        heap = [
            (-frequency, num) for num, frequency in frequencies_map.items()
        ]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
