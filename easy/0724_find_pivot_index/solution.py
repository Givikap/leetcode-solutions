class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        nums_len = len(nums)

        sums_left = [0]
        sums_right = [0] * nums_len

        for i in range(nums_len - 1):
            sums_left.append(sums_left[i] + nums[i])

        for i in range(nums_len - 2, -1, -1):
            sums_right[i] = sums_right[i + 1] + nums[i + 1]

        for i in range(nums_len):
            if sums_left[i] == sums_right[i]:
                return i

        return -1
