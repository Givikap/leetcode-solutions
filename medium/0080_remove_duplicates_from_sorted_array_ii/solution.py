from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        insert = 0
        read = 0

        while read < n:
            nums[insert] = nums[read]
            read += 1

            while read + 1 < n and nums[read + 1] == nums[insert]:
                read += 1

            insert += 1

        return insert
