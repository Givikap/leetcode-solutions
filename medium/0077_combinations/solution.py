class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combination = []
        combinations = []

        def backtrack(start: int) -> None:
            if len(combination) == k:
                combinations.append(combination[:])
                return

            for num in range(start, n + 1):
                combination.append(num)
                backtrack(num + 1)
                combination.pop()

        backtrack(1)
        return combinations
