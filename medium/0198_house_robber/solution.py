class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            rob1, rob2 = rob2, max(rob2, num + rob1)

        return rob2
