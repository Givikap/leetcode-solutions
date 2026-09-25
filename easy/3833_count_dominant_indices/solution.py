class Solution:
    def dominantIndices(self, nums: list[int]) -> int:
        postfix_sum = nums[-1]
        postfix_count = 1

        count = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] * postfix_count > postfix_sum:
                count += 1

            postfix_sum += nums[i]
            postfix_count += 1

        return count
