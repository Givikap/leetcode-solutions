class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)

        nums = sorted(num**2 for num in nums)

        score = 0

        for i in range(n // 2):
            score += nums[n - i - 1]
            score -= nums[i]

        if n % 2 == 1:
            score += nums[n // 2]

        return score
