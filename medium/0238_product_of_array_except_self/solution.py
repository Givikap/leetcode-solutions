class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        nums_len = len(nums)

        num_products = [1] * nums_len

        prefix = 1
        for i in range(nums_len):
            num_products[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(nums_len - 1, -1, -1):
            num_products[i] *= suffix
            suffix *= nums[i]

        return num_products
