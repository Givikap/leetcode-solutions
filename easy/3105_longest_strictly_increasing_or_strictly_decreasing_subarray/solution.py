class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing = False
        decreasing = False

        subbarray_size = max_subbarray_size = 1

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            num = nums[i]

            if (increasing and prev >= num) or (decreasing and prev <= num):
                increasing = False
                decreasing = False

                max_subbarray_size = max(subbarray_size, max_subbarray_size)
                subbarray_size = 1

            if not increasing and prev < num:
                increasing = True
            elif not decreasing and prev > num:
                decreasing = True

            if increasing or decreasing:
                subbarray_size += 1

        return max(subbarray_size, max_subbarray_size)
