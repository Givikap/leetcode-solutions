class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        nums.sort()
        nums_set = set(nums)

        return [
            num for num in range(nums[0], nums[-1] + 1) if num not in nums_set
        ]
