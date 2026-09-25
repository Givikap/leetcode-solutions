class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ranges = []
        range_start = nums[0]

        for prev_num, num in zip(nums, nums[1:]):
            if prev_num + 1 != num:
                ranges.append(
                    f"{range_start}->{prev_num}"
                    if range_start != prev_num
                    else str(range_start)
                )
                range_start = num

        ranges.append(
            f"{range_start}->{nums[-1]}"
            if range_start != nums[-1]
            else str(range_start)
        )
        return ranges
