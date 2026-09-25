class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closest_sum = float("inf")

        for left in range(len(nums) - 2):
            mid, right = left + 1, len(nums) - 1

            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]

                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    mid += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum

        return closest_sum
