from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(permutation: List[int], explored: List[bool]):
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
                return

            for i in range(len(nums)):
                if explored[i]:
                    continue

                permutation.append(nums[i])
                explored[i] = True

                backtrack(permutation, explored)

                permutation.pop()
                explored[i] = False

        backtrack([], [False] * len(nums))

        return permutations
