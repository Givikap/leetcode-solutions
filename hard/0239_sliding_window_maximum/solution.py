from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        max_nums = []

        for i, num in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue.popleft()

            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(i)
            max_nums.append(nums[queue[0]])

        return max_nums[k - 1 :]
