import heapq
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxHeap = []
        minHeap = [(nums[0], 0)]

        heapMap = [-1] * len(nums)
        heapMap[0] = 0

        for i in range(1, k):
            if nums[i] < minHeap[0][0]:
                heapq.heappush(maxHeap, (-nums[i], i))
                heapMap[i] = 1
            else:
                heapq.heappush(minHeap, (nums[i], i))
                heapMap[i] = 0

            if len(maxHeap) < len(minHeap) - 1:
                num, j = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-num, j))
                heapMap[j] = 1
            elif len(minHeap) < len(maxHeap):
                num, j = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, (-num, j))
                heapMap[j] = 0

        medians = []

        if k % 2 == 1:
            medians.append(minHeap[0][0])
        else:
            medians.append((-maxHeap[0][0] + minHeap[0][0]) / 2)

        staleMap = [0] * len(nums)

        maxHeapSize = len(maxHeap)
        minHeapSize = len(minHeap)

        for i in range(k, len(nums)):
            staleMap[i - k] = staleMap[i - k] + 1

            if heapMap[i - k] == 1:
                maxHeapSize -= 1
            else:
                minHeapSize -= 1

            if maxHeap and nums[i] <= -maxHeap[0][0]:
                heapq.heappush(maxHeap, (-nums[i], i))
                heapMap[i] = 1
                maxHeapSize += 1
            else:
                heapq.heappush(minHeap, (nums[i], i))
                heapMap[i] = 0
                minHeapSize += 1

            if minHeapSize > maxHeapSize + 1:
                num, j = heapq.heappop(minHeap)

                while staleMap[j]:
                    staleMap[j] -= 1
                    num, j = heapq.heappop(minHeap)

                heapq.heappush(maxHeap, (-num, j))

                heapMap[j] = 1
                maxHeapSize += 1
                minHeapSize -= 1
            elif maxHeapSize > minHeapSize:
                num, j = heapq.heappop(maxHeap)

                while staleMap[j]:
                    staleMap[j] -= 1
                    num, j = heapq.heappop(maxHeap)

                heapq.heappush(minHeap, (-num, j))

                heapMap[j] = 0
                minHeapSize += 1
                maxHeapSize -= 1

            while maxHeap and staleMap[maxHeap[0][1]]:
                staleMap[maxHeap[0][1]] -= 1
                heapq.heappop(maxHeap)
            while minHeap and staleMap[minHeap[0][1]]:
                staleMap[minHeap[0][1]] -= 1
                heapq.heappop(minHeap)

            if (maxHeapSize + minHeapSize) % 2 == 1:
                medians.append(minHeap[0][0])
            else:
                medians.append((-maxHeap[0][0] + minHeap[0][0]) / 2)

        return medians
