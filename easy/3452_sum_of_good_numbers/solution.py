class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        good_numbers_sum = 0

        for i in range(len(nums)):
            if i - k >= 0 and nums[i] <= nums[i - k]:
                continue
            if i + k < len(nums) and nums[i] <= nums[i + k]:
                continue

            good_numbers_sum += nums[i]

        return good_numbers_sum
