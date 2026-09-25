class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        nums_len = len(nums)

        four_sums = []

        for outer_left in range(nums_len - 3):
            if outer_left > 0 and nums[outer_left] == nums[outer_left - 1]:
                continue

            if (
                nums[outer_left]
                + nums[outer_left + 1]
                + nums[outer_left + 2]
                + nums[outer_left + 3]
                > target
            ):
                break
            if nums[outer_left] + nums[-3] + nums[-2] + nums[-1] < target:
                continue

            for inner_left in range(outer_left + 1, nums_len - 2):
                if (
                    inner_left > outer_left + 1
                    and nums[inner_left] == nums[inner_left - 1]
                ):
                    continue

                if (
                    nums[outer_left]
                    + nums[inner_left]
                    + nums[inner_left + 1]
                    + nums[inner_left + 2]
                    > target
                ):
                    break
                if (
                    nums[outer_left] + nums[inner_left] + nums[-2] + nums[-1]
                    < target
                ):
                    continue

                inner_right = inner_left + 1
                outer_right = nums_len - 1

                left_sum = nums[outer_left] + nums[inner_left]

                while inner_right < outer_right:
                    curr_sum = left_sum + nums[inner_right] + nums[outer_right]

                    if curr_sum == target:
                        four_sums.append(
                            (
                                nums[outer_left],
                                nums[inner_left],
                                nums[inner_right],
                                nums[outer_right],
                            )
                        )

                        while (
                            inner_right < outer_right
                            and nums[inner_right] == nums[inner_right + 1]
                        ):
                            inner_right += 1
                        while (
                            inner_right < outer_right
                            and nums[outer_right] == nums[outer_right - 1]
                        ):
                            outer_right -= 1

                        inner_right += 1
                        outer_right -= 1
                    elif curr_sum < target:
                        inner_right += 1
                    else:
                        outer_right -= 1

        return four_sums
