class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)

        curr_i = max_i = 0
        jumps = 0

        for i in range(n - 1):
            max_i = max(max_i, i + nums[i])

            if i == curr_i:
                curr_i = max_i
                jumps += 1

        return jumps
