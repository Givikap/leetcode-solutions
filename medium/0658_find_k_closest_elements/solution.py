from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        left = bisect_left(arr, x)
        right = left

        while right - left < k:
            if left != 0 and right != n:
                if x - arr[left - 1] <= arr[right] - x:
                    left -= 1
                else:
                    right += 1
            elif right == n:
                left -= 1
            else:
                right += 1

        neighbors = []

        for i in range(left, right):
            neighbors.append(arr[i])

        return neighbors
