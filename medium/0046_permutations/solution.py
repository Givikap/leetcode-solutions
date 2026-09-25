class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []

        def backtrack(permutation: list[int], explored: list[bool]):
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
