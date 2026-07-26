from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        minDifference = float("inf")
        differences = []

        for i in range(len(arr) - 1):
            currDifference = arr[i + 1] - arr[i]

            if currDifference == minDifference:
                differences.append((arr[i], arr[i + 1]))
            elif currDifference < minDifference:
                differences = [(arr[i], arr[i + 1])]
                minDifference = currDifference

        return differences
