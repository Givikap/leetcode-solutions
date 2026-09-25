class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        return len(heights) - sum(
            height == expected
            for height, expected in zip(heights, sorted(heights))
        )
