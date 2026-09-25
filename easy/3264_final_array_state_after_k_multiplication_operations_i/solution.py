import heapq


class Solution:
    def getFinalState(
        self, nums: list[int], k: int, multiplier: int
    ) -> list[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            num, i = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, i))

        for num, i in heap:
            nums[i] = num

        return nums
