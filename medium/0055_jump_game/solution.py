class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_i = 0

        for i, jump in enumerate(nums):
            if i > max_i:
                return False
            max_i = max(max_i, i + jump)

        return True
