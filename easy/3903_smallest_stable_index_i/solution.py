class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        nums_len = len(nums)

        prefix_maxes = [nums[0]] * nums_len
        prefix_mins = [nums[nums_len - 1]] * nums_len

        for i in range(1, nums_len):
            prefix_maxes[i] = max(prefix_maxes[i - 1], nums[i])

        for i in range(nums_len - 2, -1, -1):
            prefix_mins[i] = min(prefix_mins[i + 1], nums[i])

        for i in range(nums_len):
            if prefix_maxes[i] - prefix_mins[i] <= k:
                return i

        return -1
