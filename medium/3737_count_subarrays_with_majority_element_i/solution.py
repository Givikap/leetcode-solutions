class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        count = 0

        for i in range(n):
            targetCount = 0

            for j in range(i, n):
                if nums[j] == target:
                    targetCount += 1
                else:
                    targetCount -= 1

                if targetCount > 0:
                    count += 1

        return count
